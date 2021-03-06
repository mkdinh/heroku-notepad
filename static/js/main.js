function fetchTasks() {
  d3.json("/tasks").then((tasks) => {
    var list = d3.select("#tasks");
    list.html("");

    tasks.forEach((task) => {
      var item = list.append("li");
      item.classed("list-group-item", true);
      item.text(task.description);
    });
  });
}

fetchTasks();
