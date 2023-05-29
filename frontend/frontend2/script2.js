const countAntInput = document.getElementById("countAntInput");
const countWayInput = document.getElementById("countWayInput");
const countStartInput = document.getElementById("countStartInput");
const countMoveInput = document.getElementById("countMoveInput");

document.getElementById("getDataBtn").addEventListener("click", () => {
  fetch("/getData")
    .then(response => response.json())
    .then(data => {
      countAntInput.value = data.count_ant;
      countWayInput.value = data.count_way;
      countStartInput.value = data.count_start;
      countMoveInput.value = data.count_move;
    })
    .catch(error => console.error(error));
});
