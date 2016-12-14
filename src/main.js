window.App = {
    Helper: {},
    Router: {},
    Model: {},
    Collection: {},
    View: {},
    Form: {}
};

global.$ = global.jQuery = require('jquery');
var Backbone = require('backbone');
Backbone.$ = $;

// we do need this for dustjs helpers!!!
require('dustjs-helpers');
require('./dust-filters.js');

var Router = require('./router.js');

var swap = require('./views/swap.js');
var Regions = require('./views/regions.js');
var NavigationView = require('./views/navigation.js');


// global key shortcuts
var key = require('keymaster');

key('s', function () {
    $('input[type=search]').focus();
    return false; // prevent writing of 's'
});

key('h', function () {
    App.Router.r.navigate('/', {trigger: true});
});

key('a', function () {
    App.Router.r.navigate('/archive', {trigger: true});
});

key('t', function () {
    App.Router.r.navigate('/timeline', {trigger: true});
});


(function($) {
    $.QueryString = (function(a) {
        if (a == "") return {};
        var b = {};
        for (var i = 0; i < a.length; ++i)
        {
            var p=a[i].split('=', 2);
            if (p.length != 2) continue;
            b[p[0]] = decodeURIComponent(p[1].replace(/\+/g, " "));
        }
        return b;
    })(window.location.search.substr(1).split('&'))
})(jQuery);

// jquery attr() functionality
// usage:
// var $div = $("<div data-a='1' id='b'>");
// $div.attr();  // returning { "data-a": "1", "id": "b" }
(function (old) {
    $.fn.attr = function () {
        if (arguments.length === 0) {
            if (this.length === 0) {
                return null;
            }

            var obj = {};
            $.each(this[0].attributes, function () {
                if (this.specified) {
                    obj[this.name] = this.value;
                }
            });
            return obj;
        }
        return old.apply(this, arguments);
    };
})($.fn.attr);


$(function () {
    // set the csrftoken
    //Backbone.Tastypie.csrfToken = Cookies.get('csrftoken');

    // catch 401
    $(document).ajaxError(function (event, xhr) {
        if (xhr.status == 401) {
            // window.location = '/login';
            console.log("LOGIN!");
        }
    });

    Backbone.History.prototype.navigate = _.wrap(Backbone.History.prototype.navigate, function () {
        // Get arguments as an array
        var args = _.toArray(arguments);
        // firs argument is the original function
        var original = args.shift();
        // Set the before event
        Backbone.history.trigger('before:url-change', args);
        // Call original function
        var res = original.apply(this, args);
        // After event
        Backbone.history.trigger('url-changed');
        // Return original result

        return res;
    });

    Backbone.history.bind('before:url-change', function (path, e) {
        // console.log("before url change", path, e);
    });

    Backbone.history.bind('url-changed', function () {
        //console.warn("url-changed");
        window.scrollTo(0, 0); // scroll to top on url change! TODO: finer control when to scroll top ie. when navigation from detail to list views that were scrolled before...

        // if (App.currentView.viewState && typeof(App.currentView.viewState.get('scrollPosition')) !== 'undefined') {
        //$(document).scrollTop(App.currentView.viewState.get('scrollPosition'));
        //}

    });


    /*
     App.currentView = false;
     $(window).on('scroll', function () {
     // Not all views will be interested in maintaining scroll position, so we need to check them first.
     if (App.currentView.viewState && typeof(App.currentView.viewState.get('scrollPosition')) !== 'undefined') {
     //console.warn('setting scrollPosition ', App.currentView.viewState.attributes, $(document).scrollTop());
     App.currentView.viewState.set('scrollPosition', $(document).scrollTop());
     }
     });
     */

    $(document).on('click', 'a:not([data-bypass])', function (evt) {

        var href = $(this).attr('href');
        var protocol = this.protocol + '//';

        if (href.slice(protocol.length) !== protocol) {
            evt.preventDefault();
            App.Router.r.navigate(href, {trigger: true});
        }
    });


    App.Router.r = new Router();
    var navigation = new NavigationView({});

    App.Router.r.on('route', function (route, params) {
        navigation.render();
        navigation.onShow();
    });
    Backbone.history.start({pushState: true});


    swap(Regions.navigation, navigation);

});


