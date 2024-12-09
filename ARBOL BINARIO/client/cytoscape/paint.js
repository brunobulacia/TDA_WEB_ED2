import { cy, initializeCytoscape } from "/client/cytoscape/graph.js";
import { getNodes, getRoot } from "/client/js/connection.js";
let nodes = [];
let edges = [];

export async function inicializarGrafo() {
  await initializeCytoscape();
  await addVertices();
  await addAristas();
  ajustarGrafo();
}

export async function addVertices() {
  const root = await getRoot();
  const nodos = await getNodes();
  nodes.push({
    data: {
      id: String(root),
    },
    position: { x: 100, y: -40 },
  });
  nodos.forEach((node) => {
    nodes.push({
      data: {
        id: String(node[0]),
      },
      position: { x: 0, y: 0 },
    });
  });
  console.log(nodes);
  cy.add(nodes);
}

export async function addAristas() {
  const nodos = await getNodes();
  nodos.forEach((node) => {
    edges.push({
      data: {
        id: String(node[1]) + "-" + String(node[0]),
        source: String(node[1]), // El padre
        target: String(node[0]), // El nodo actual
      },
    });
  });
  cy.add(edges);
  console.log(edges);
}

async function ajustarGrafo() {
  const nodos = await getNodes();
  let horizontalSpacing = Math.pow(2, nodos[nodos.length - 1][2] + 4);
  let verticalSpacing = 50; //
  let rootX = 500; // Posición inicial de la raíz en el eje X (mantener o ajustar)
  let rootY = 50; // Posición inicial de la raíz en el eje Y (mantener o ajustar)
  // Recorrer cada nodo para posicionarlos
  nodos.forEach((node) => {
    let parent = cy.getElementById(String(node[1])); // Obtener el nodo padre
    let child = cy.getElementById(String(node[0])); // Obtener el nodo hijo
    let posX, posY;
    let posParent = parent.position();
    posY = posParent.y + verticalSpacing; // El hijo siempre estará debajo del padre, con menos altura
    // Ajustamos el espaciado horizontal según el nivel del nodo
    let depth = node[2]; // La profundidad del nodo
    let levelSpacing = horizontalSpacing / Math.pow(2, depth); // Reducimos el espacio con la profundidad

    if (node[0] < node[1]) {
      // El hijo es menor que el padre, va a la izquierda
      posX = posParent.x - levelSpacing;
    } else {
      // El hijo es mayor que el padre, va a la derecha
      posX = posParent.x + levelSpacing;
    }
    // Actualizamos la posición del nodo hijo
    child.position({ x: posX, y: posY });
  });
}

export function searchNodePaint(e) {
  let foundNode = null;
  foundNode = cy.getElementById(e);
  if (foundNode) {
    foundNode.style("background-color", "#ffff00");
  }
  setTimeout(() => {
    foundNode.style("background-color", "#1A7F8F");
  }, 2000);
}
