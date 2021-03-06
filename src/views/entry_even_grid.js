var Backbone = require('backbone');
var _ = require('underscore');
var $ = require('jquery');
Backbone.$ = $;


var Base = require('./base');
var EntryEvenGridSingleView = require('./entry_even_grid_single');

var swap = require('../views/swap.js');


module.exports = Base.ListView.extend({

    template: require('../templates/entry_even_grid.dust'),

    addOne: function (model) {
        //console.debug('add', model.id);
        if (this.data.num_columns == undefined)
            var cols = 4;
        else
            var cols = this.data.num_columns;
        var view = new EntryEvenGridSingleView({model: model, data: {num_columns: cols}});
        this.$(".entries").append(view.render().el);
        view.onShow(); // TODO call onShow automatically
    },

});