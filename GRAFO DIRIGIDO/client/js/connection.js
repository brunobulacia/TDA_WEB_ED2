export async function vaciarGrafoAPI() {
  try {
    const response = await fetch("http://localhost:5000/vaciar", {
      method: "POST",
    });
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || "Error en la respuesta del servidor");
    }
    const data = await response.json();
    console.log(data);
  } catch (error) {
    alert("Error al conectar con el servidor: " + error.message);
    return null;
  }
}

export async function getGrafoAPI() {
  try {
    const response = await fetch("http://localhost:5000/get_grafo");
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || "Error en la respuesta del servidor");
    }
    const data = await response.json();
    // console.log(data);
    return data;
  } catch (error) {
    alert("Error al conectar con el servidor: " + error.message);
    return null;
  }
}

export async function addAristaAPI(v1, v2, peso) {
  try {
    const response = await fetch("http://localhost:5000/add_arista", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ v1, v2, peso }),
    });
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || "Error en la respuesta del servidor");
    }
    const data = await response.json();
    // console.log(data);
    return data;
  } catch (error) {
    alert("Error al conectar con el servidor: " + error.message);
    return null;
  }
}

export async function addVerticeAPI(v) {
  try {
    console.log(v);
    const response = await fetch("http://localhost:5000/add_vertice", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ v }),
    });
    if (!response.ok) {
      const errorData = await response.json();
      console.log(errorData);
      throw new Error(errorData.error || "Error en la respuesta del servidor");
    }
    const data = await response.json();
    // console.log(data);
    return data;
  } catch (error) {
    alert("Error al conectar con el servidor: " + error.message);
    return null;
  }
}

export async function removeAristaAPI(v1, v2) {
  try {
    const response = await fetch("http://localhost:5000/remove_arista", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ v1, v2 }),
    });
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || "Error en la respuesta del servidor");
    }
    const data = await response.json();
    // console.log(data);
    return data;
  } catch (error) {
    alert("Error al conectar con el servidor: " + error.message);
    return null;
  }
}

export async function removeVerticeAPI(v) {
  try {
    const response = await fetch("http://localhost:5000/remove_vertice", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ v }),
    });
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || "Error en la respuesta del servidor");
    }
    const data = await response.json();
    // console.log(data);
    return data;
  } catch (error) {
    alert("Error al conectar con el servidor: " + error.message);
    return null;
  }
}
