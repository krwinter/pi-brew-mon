define([
  "backbone",
  "marionette", 
  "epoxy"
  ], function(
  Backbone, 
  Marionette, 
  Epoxy
  ) {

  // Base set of functions that can be mixed into standard views such as ItemViews, CompositeViews, etc.

  //var mixin = Marionette.Object.extend({
  var mixin = {

    epoxyBindingEnabled: true,

    initialize: function(options) {
      if (this.epoxyBindingEnabled) {
        this.epoxify();
      }
      this.triggerMethod("initialize");
    },

    epoxify: function() {
      Epoxy.View.mixin(this);
      this.listenTo(this, "ui:bind", this.applyBindings);
      this.listenTo(this, "before:close", this.removeBindings);
    },

    // Override Marionette's impl so we can trigger our own event
    bindUIElements : function() {
      this.trigger("ui:bind");
      Marionette.View.prototype.bindUIElements.apply(this, arguments);
    }

  };

  return mixin;

});