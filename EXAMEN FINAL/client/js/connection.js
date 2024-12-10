export async function consumeAPI() {
  try {
    const response = await fetch("http://localhost:5000/");
    const { lista } = await response.json();
    console.log(lista);
    return lista;
  } catch (error) {
    console.error("Error:", error);
    return null;
  }
}
