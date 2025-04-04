document.addEventListener("DOMContentLoaded", () => {
  fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")
    .then((response) => response.json())
    .then((data) => {
      document.getElementById("hello").textContent = data.hello;
    })
    .catch((error) => {
      console.error("Error:", error);
    });
});
