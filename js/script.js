const currentDate = new Date();
const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
const formattedDate = currentDate.toLocaleDateString('en-GB', options);
document.getElementById("DayOfTheWeek").innerHTML = formattedDate;


// Data for the pie chart
const data = {
  labels: ['Meetings', 'Time in Office', 'Development', 'Training'],
  datasets: [{
    label: 'Percentage',
    data: [12, 19, 13, 20],
    backgroundColor: [
      '#FBD4F5',
      '#E5D6FB',
      '#D5E4FA',
      '#FFFDC7',
    ],
    hoverOffset: 4
  }]
};

// Configuration options
const config = {
  type: 'pie',
  data: data,
};

// Create the pie chart
var myPieChart = new Chart(
  document.getElementById('myPieChart'),
  config
);