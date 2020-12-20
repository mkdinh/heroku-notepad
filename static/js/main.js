function loadTasks() {
  d3.json("/api/tasks").then((tasks) => {
    var listGroup = d3.select("#tasks");
    listGroup.html("");

    tasks.forEach((task) => {
      var listItem = listGroup.append("li");
      listItem.attr("class", "list-group-item");
      listItem.text(task.description);
    });
  });
}

loadTasks();
