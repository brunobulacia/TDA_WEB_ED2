let nodes;

export async function getTreeAPI() {
  try {
    const response = await fetch("http://localhost:5000/get_tree");
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || "Error en la respuesta del servidor");
    }
    const data = await response.json();
    // console.log(data);
    return data;
  } catch (error) {
    alert("Error al conectar con el servidor" + error);
    return null;
  }
}

// Función para obtener la raíz del árbol
export async function getRoot() {
  nodes = await getTreeAPI();
  console.log(nodes);
  if (nodes && nodes.length > 0) {
    console.log(nodes[0][0]);
    return nodes[0][0];
  } else {
    throw new Error("No hay nodos disponibles en el árbol.");
  }
}
/*
// Función para obtener todos los nodos del árbol (excepto la raíz)
export async function getNodes() {
  // nodes = await getTreeAPI();
  if (nodes) {
    return nodes.slice(1, nodes.length);
  } else {
    throw new Error("No hay nodos disponibles en el árbol.");
  }
}

export async function getCantNodesAPI() {
  if (nodes && nodes.length > 0) {
    return nodes.length;
  }
  alert("No hay nodos disponibles en el árbol.");
}

export async function getHeightAPI() {
  if (nodes) {
    return nodes[nodes.length - 1][2];
  }
  alert("No hay nodos disponibles en el árbol.");
}

export async function vaciarTreeAPI() {
  try {
    const response = await fetch("http://localhost:5000/vaciar");
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || "Error en la respuesta del servidor");
    }
    const data = await response.json();
    return data;
  } catch (error) {
    alert(error);
    return null;
  }
} */

export async function insertarDatoAPI(nodo) {
  try {
    console.log(JSON.stringify({ nodo }));
    const response = await fetch("http://localhost:5000/insertar_dato", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ nodo }),
    });
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || "Error en la respuesta del servidor");
    }
    const responseData = await response.json();
    return responseData;
  } catch (error) {
    alert(error);
    return null;
  }
}

export async function deleteNodeAPI(nodo) {
  try {
    const response = await fetch("http://localhost:5000/eliminar_dato", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ nodo }),
    });
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || "Error en la respuesta del servidor");
    }
    const responseData = await response.json();
    return responseData;
  } catch (error) {
    alert(error);
    return null;
  }
}
