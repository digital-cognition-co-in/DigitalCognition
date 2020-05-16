var elementCount = 0;
var jsPlumbInstance; //the jsPlumb jsPlumbInstance
jsPlumb.ready(function () {
 
    jsPlumbInstance = window.jsp = jsPlumb.getInstance({
        // default drag options
        DragOptions: {
            cursor: 'pointer',
            zIndex: 2000
        },
        //the arrow overlay for the connection
        ConnectionOverlays: [
            ["Arrow", {
                location: 1,
                visible: true,
                id: "ARROW";
            }]
        ],
        Container: "canvas";
    });
 
    //define basic connection type

    var basicType = {
        connector: "StateMachine",
        paintStyle: {strokeStyle:"#216477", lineWidth: 4},
        hoverPaintStyle: {strokeStyle: "blue"}
    };
    jsPlumbInstance.registerConnectionType("basic", basicType);
 
    //style for the connector
    var connectorPaintStyle = {
        lineWidth: 4,
        strokeStyle: "#61B7CF",
        joinstyle: "round",
        outlineColor: "white",
        outlineWidth: 2
    },
    //style for the connector hover
        connectorHoverStyle = {
            lineWidth: 4,
            strokeStyle: "#216477",
            outlineWidth: 2,
            outlineColor: "white"
        },
        endpointHoverStyle = {
            fillStyle: "#216477",
            strokeStyle: "#216477"
},
 
    //the source endpoint definition from which a connection can be started
        sourceEndpoint = {
            endpoint: "Dot",
            paintStyle: {
                strokeStyle: "#7AB02C",
                fillStyle: "transparent",
                radius: 7,
                lineWidth: 3
            },
            isSource: true,
            connector: ["Flowchart", {stub: [40, 60], gap: 5, cornerRadius: 5, alwaysRespectStubs: true}],
            connectorStyle: connectorPaintStyle,
            hoverPaintStyle: endpointHoverStyle,
            connectorHoverStyle: connectorHoverStyle,
            EndpointOverlays: [],
            maxConnections: -1,
            dragOptions: {},
            connectorOverlays: [
                ["Arrow", {
                    location: 1,
                    visible: true,
                    id: "ARROW",
                    direction: 1
                }]
            ]
        },
 
    //definition of the target endpoint the connector would end
    targetEndpoint = {
        endpoint: "Dot",
        paintStyle: {fillStyle: "#7AB02C", radius: 9},
        maxConnections: -1,
        dropOptions: {hoverClass: "hover", activeClass: "active"},
        hoverPaintStyle: endpointHoverStyle,
        isTarget: true
    };

function makeDraggable(id, className, text){
    $(id).draggable({
        helper: function(){
            return $("<div/>",{
                text: text,
                class:className
            });
        },
        stack: ".custom",
        revert: false
    });
}


makeDraggable("#startEv", "window start jsplumb-connected custom", "start");
makeDraggable("#stepEv", "window step jsplumb-connected-step custom", "step");
makeDraggable("#endEv", "window start jsplumb-connected-end custom", "end");

$("#canvas").droppable({
     accept: ".window",
     drop: function (event, ui) {
         ui.helper.clone().appendTo(this);
     }
});


