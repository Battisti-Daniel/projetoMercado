const submit = document
  .getElementById("submit")
  .addEventListener("submit", function (ev) {
    ev.preventDefault;
    const date = document.getElementById("date").value;
    console.log(date);
    alert("Funcionario cadastrado com sucesso!");
  });
