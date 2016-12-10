//----------------------------------------------------------------------------------
(function () {
//----------------------------------------------------------------------------------
Ext.application({
    requires: ['Ext.container.Viewport'],
    name: 'TransitHound',

    appFolder: 'app',

    launch: function() {  
    	Ext.ns("app$");
    	
    	app$.routeListController = Ext.create("TransitHound.RouteListController", {});
    	app$.routeListController.init();

    	app$.routeMapController = Ext.create("TransitHound.RouteMapController", {});
    	app$.routeMapController.init();
    	
    	app$.mainPanel = Ext.create('Ext.panel.Panel', {
    	    renderTo: Ext.getBody(),
            title: 'TransitHound',
            layout:{
                type: 'hbox'
            },
    	    width: window.innerWidth,
    	    height: window.innerHeight,
    	    listeners: {
    	    	destroy: function() {
        			console.log(": event: destroy: panel: ");
    	    	}
    	    },
    		onDestroy: function() {
	    		console.log(": onDestroy: panel: ");
    		},
    	    items: [
    	    	app$.routeListController.routeListPanel,
    	    	{xtype: "splitter"},
    	    	app$.routeMapController.routeMapPanel
    	    ]
    	});
    	
    	app$.routeMapController.getGMapPanel().addListener(
    		"mapready",
    		function () {
    			console.log(": GMapPanel ready: ");
    			
    			app$.routeMapController.getGMapPanel().addFusionTablesLayer("*", "1sp1YKyolOo5y8om7NSUEmLOYOK09aBcdxELQlVXY");
    		},
    		this
    	);
    	
    	app$.mainPanel.show();
    }
});

//----------------------------------------------------------------------------------
}());