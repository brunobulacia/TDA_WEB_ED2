export let cy;
export function initializeCytoscape() {
  cy = cytoscape({
    container: document.getElementById("cy"), // container to render in
    elements: [],
    style: [
      // Estilo para nodos
      {
        selector: "node",
        style: {
          "background-color": "#1A7F8F", // Azul oscuro como color base
          "border-width": 3,
          "border-color": "#3B12F6", // Azul más claro para bordes
          "text-halign": "center",
          "text-valign": "center",
          label: "data(id)", // Mostrar el nombre del estado
          "font-size": 14,
          "font-weight": "bold",
          color: "#FFFFFF", // Texto blanco
          width: 32,
          height: 32,
          "text-outline-color": "#1E3A8A", // Contorno de texto para mayor visibilidad
        },
      },

      // Estilo para aristas
      {
        selector: "edge",
        style: {
          width: 4,
          "line-color": "#F59E0B", // Naranja complementario para las aristas
          "target-arrow-color": "#F59E0B", // Flechas del mismo color
          "target-arrow-shape": "triangle",
          "curve-style": "bezier", // Líneas curvas
          // label: "data(id)", // Mostrar etiquetas de las aristas (si se usan)
          "font-size": 12,
          color: "#1E3A8A", // Texto azul oscuro para contraste
          "text-background-opacity": 1,
          "text-background-color": "#FFFFFF", // Fondo blanco para texto
          "text-border-color": "#3B82F6",
          // "text-border-width": 1,
          "text-rotation": "autorotate",
          "text-margin-y": -8, // Ajustar posición del texto
        },
      },
    ],

    minZoom: 1, // Zoom mínimo
    maxZoom: 1.2, // Zoom máximo
  });

  // Ajustar la vista inicial
  cy.fit();
  cy.viewport({
    zoom: 1.2,
    pan: { x: 500, y: 100 },
  });
}
