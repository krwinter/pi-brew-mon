//var Dispatcher = require('flux').Dispatcher;
var AppDispatcher = require('./appDispatcher');
var Api = require('./fermApi');
var Store = require('./fermStore');

// tutorial2.js
var FermControl = React.createClass({

	getInitialState: function() {
		//Api.getFermData();
		return {data: []};
	},

	componentDidMount: function() {

		console.log('MOUNT');
		this.setState({currentTemp: 25.5, setTemp: 25});
		//debugger
		//Store.addChangeListener(this._onChange);
		Store.on('change', this._onChange, this).bind(this);
		Api.getFermData();
	},

	componentWillUnmount: function() {
		//store.removeChangeListener(this._onChange);
		Store.off(null, null, this);
	},

	render: function() {
		return (
				<div className="fermControl">
					<div className="header">
						Fermentation Temperature Control
					</div>
					<div className="currentTemp">
						Current Temp: {this.state.currentTemp}
					</div>
					<div className="setTemp">
						Current Temp: {this.state.setTemp}
					</div>
					<div className="status">
						Status: {this.state.status}
					</div>
				</div>
		);
	},

	_onChange: function() {
		//debugger
		this.setState(Store.getFermState());
	}
});

module.exports = FermControl;
