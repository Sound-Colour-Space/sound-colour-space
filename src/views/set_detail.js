var Backbone = require('backbone');

var _ = require('underscore');

Backbone.$ = $;

var Base = require('./base');
var swap = require('./swap');
var EntryListView = require('./entry_list');
var EntryGridView = require('./entry_grid');
var EntryEvenGridView = require('./entry_even_grid');

var helper = require('../helpers/helper.js');

var marked = require('marked');

var renderer = new marked.Renderer();

// override link rendering
renderer.link = function (href, title, text) {

    if (href.indexOf('http://') === 0 || href.indexOf('https://') === 0) {
        return '<a href="' + href + '" title="' + (title != null ? title : "") + '" target="_blank" data-bypass>' + text + '</a>';
    } else {
        return '<a href="' + href + '" title="' + (title != null ? title : "") + '">' + text + '</a>';
    }
};

module.exports = Base.DetailView.extend({

    template: require('../templates/set_detail.dust'),

    data: {
        preferredView: 'list'
    },

    onShow: function () {

        // create a collection based on entries
        this.collection = new Backbone.Collection(this.model.get('entry'));

        if (!App.preferredView)
            App.preferredView = 'list';

        if (App.preferredView === 'list') {
            var view = new EntryListView({collection: this.collection});
        }

        else if (App.preferredView === 'grid') {
            var view = new EntryGridView({collection: this.collection});
        }

        else {
            var view = new EntryEvenGridView({
                collection: this.collection,
                data: {num_columns: this.model.get('num_columns')}
            });
        }

        MathJax.Hub.Queue(
            ["Typeset", MathJax.Hub, "description"],
            function () {
                $('.set.description').html(marked($('.set.description').html(), {renderer: renderer}));
                $('.set.description').css('opacity', '1');
                swap($('[data-js-region="entry_list"]'), view);
            }
        );


        //helper.scrollToPosition(App.Helper.offsetTop);


    },

    events: {
        // change views
        'click .toggle-list': function () {
            App.preferredView = "list";
            this.data.preferredView = App.preferredView;
            // instead of calling render() we do rendering here because of flickering (mathjax+markdown)
            $('.button.toggle-list').addClass('active');
            $('.button.toggle-grid').removeClass('active');
            $('.button.toggle-even-grid').removeClass('active');
            var view = new EntryListView({collection: this.collection});
            swap($('[data-js-region="entry_list"]'), view);
            Cookies.set('preferredView', 'list');
        },

        'click .toggle-even-grid': function () {
            App.preferredView = "even-grid";
            this.data.preferredView = App.preferredView;
            // instead of calling render() we do rendering here because of flickering (mathjax+markdown)
            $('.button.toggle-even-grid').addClass('active');
            $('.button.toggle-grid').removeClass('active');
            $('.button.toggle-list').removeClass('active');
            var view = new EntryEvenGridView({
                collection: this.collection,
                data: {num_columns: this.model.get('num_columns')}
            });
            swap($('[data-js-region="entry_list"]'), view);
            Cookies.set('preferredView', 'even-grid');
        },
        'click .toggle-grid': function () {
            App.preferredView = "grid";
            this.data.preferredView = App.preferredView;
            // instead of calling render() we do rendering here because of flickering (mathjax+markdown)
            $('.button.toggle-grid').addClass('active');
            $('.button.toggle-even-grid').removeClass('active');
            $('.button.toggle-list').removeClass('active');
            var view = new EntryGridView({collection: this.collection});
            swap($('[data-js-region="entry_list"]'), view);
            Cookies.set('preferredView', 'grid');
        },

    },

});

