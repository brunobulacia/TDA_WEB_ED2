export let cy;
export function initializeCytoscape() {
  cy = cytoscape({
    container: document.getElementById("cy"), // container to render in
    elements: [
      {
        data: { id: "q0" },
        position: { x: 50, y: 50 },
      },
      {
        data: { id: "q1" },
        position: { x: 200, y: 50 },
      },
      {
        data: { id: "q2" },
        position: { x: 350, y: 50 },
      },
      {
        data: { id: "q3" },
        position: { x: 500, y: 50 },
      },
      {
        data: { id: "q4" },
        position: { x: 650, y: 50 },
      },
      {
        data: { id: "q5" },
        position: { x: 800, y: 50 },
      },
      {
        data: { id: "q6" },
        position: { x: 950, y: 50 },
      },
      {
        data: { id: "q7" },
        position: { x: 1100, y: 50 },
      },
      {
        data: { id: "q8" },
        position: { x: 1250, y: 50 },
      },
      {
        data: { id: "q9" },
        position: { x: 1400, y: 50 },
      },
      {
        data: { id: "q10" },
        position: { x: 1550, y: 50 },
      },
      {
        data: { id: "q11" },
        position: { x: 1700, y: 50 },
      },
      {
        data: { id: "q12" },
        position: { x: 1850, y: 50 },
      },
      {
        data: { id: "q13" },
        position: { x: 2000, y: 50 },
      },
      {
        data: { id: "q14" },
        position: { x: 2150, y: 50 },
      },
      {
        data: { id: "q15" },
        position: { x: 2300, y: 50 },
      },
      {
        data: { id: "q16" },
        position: { x: 2450, y: 50 },
      },
    ],
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
          "font-size": 16,
          "font-weight": "bold",
          color: "#FFFFFF", // Texto blanco
          width: 50,
          height: 50,
          "text-outline-color": "#1E3A8A", // Contorno de texto para mayor visibilidad
          "text-outline-width": 2,
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
          "font-size": 18,
          color: "#1E3A8A", // Texto azul oscuro para contraste
          "text-background-opacity": 0,
          "text-background-color": "#FFFFFF", // Fondo blanco para texto
          "text-border-color": "#3B82F6",
          "text-border-width": 1,
          "text-rotation": "autorotate",
          "text-margin-y": -8, // Ajustar posición del texto
          "text-margin-x": 10,
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
