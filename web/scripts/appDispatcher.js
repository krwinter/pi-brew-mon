

// module.exports = AppDispatcher;
// var assign = require('object-assign');
// var Dispatcher = require('flux').Dispatcher;

// var AppDispatcher = assign({}, Dispatcher.prototype, {

//   *
//    * A bridge function between the views and the dispatcher, marking the action
//    * as a view action.  Another variant here could be handleServerAction.
//    * @param  {object} action The data coming from the view.
   
//   handleAction: function(action) {
//     this.dispatch({
//       source: 'SERVER_ACTION',
//       action: action
//     });
//   }

// });

//module.exports = AppDispatcher;


var Dispatcher = require('flux').Dispatcher;

var AppDispatcher = new Dispatcher();

module.exports = AppDispatcher;