// Function to toggle fullscreen images
function toggleFullScreen(img) {
    let fullscreenDiv = document.getElementById("fullscreen-container");

    if (fullscreenDiv) {
        fullscreenDiv.remove();
        document.body.style.overflow = "auto";
    } else {
        fullscreenDiv = document.createElement("div");
        fullscreenDiv.id = "fullscreen-container";
        fullscreenDiv.style = `
            position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
            background: rgba(0, 0, 0, 0.9); display: flex;
            justify-content: center; align-items: center; cursor: pointer;
            z-index: 1000;
        `;

        let fullscreenImg = document.createElement("img");
        fullscreenImg.src = img.src;
        fullscreenImg.style = "max-width: 90vw; max-height: 90vh; object-fit: contain;";

        fullscreenDiv.appendChild(fullscreenImg);
        document.body.appendChild(fullscreenDiv);
        document.body.style.overflow = "hidden";

        fullscreenDiv.onclick = () => {
            fullscreenDiv.remove();
            document.body.style.overflow = "auto";
        };
    }
}

// Function to change the interactive graph
function changeGraph(year) {
    document.getElementById('rainfall-graph').data = `images/rainfall_graph_${year}.svg`;
}


// travel form

// Rainfall data for each month in mm (not accurate)
const rainfallData = {
  January: 50,
  February: 50,
  March: 70,
  April: 90,
  May: 120,
  June: 200,
  July: 230,
  August: 250,
  September: 250,
  October: 220,
  November: 70,
  December: 40
};

// Event listener for the form submission
document.getElementById('travelForm').addEventListener('submit', function(event) {
  event.preventDefault(); // Prevent the form from submitting and refreshing the page

  // Collect form data (name, selected month, email, and years)
  const name = document.getElementById('name').value;
  const month = document.getElementById('month').value;
  const email = document.getElementById('email').value;
  const receiveData = document.querySelector('input[name="receiveData"]:checked').value === 'true'; // Boolean for receiving data
  const years = receiveData ? document.getElementById('years').value : null; // Integer: Years if they want data

  // Validate the data to make sure all fields are filled in
  if (!name || !month || !email || (receiveData && !years)) {
    alert('All fields are required!');
    return;
  }

  // Save the collected data to localStorage (for simplicity)
  const userData = {
    name: name,
    month: month,
    email: email,
    receiveData: receiveData,
    years: years
  };

  // Store the data as a string in localStorage
  localStorage.setItem('userData', JSON.stringify(userData));

  // Prepare the summary text to display to the user
  const summaryText = `Name: ${name}<br>Month: ${month}<br>Email: ${email}<br>Receive Data: ${receiveData ? 'Yes' : 'No'}`;
  document.getElementById('summaryText').innerHTML = summaryText;

  // If the user wants data, include the years they are interested in
  if (receiveData) {
    document.getElementById('summaryText').innerHTML += `<br>Years Interested: ${years}`;
  }

  // Get a recommendation based on the selected month
  const recommendationText = getRecommendation(month);

  // Display the recommendation
  document.getElementById('recommendation').innerHTML = recommendationText;

  // Show the summary and recommendation section
  document.getElementById('summary').style.display = 'block';

  // Reset the form fields after submission
  document.getElementById('travelForm').reset();
  document.getElementById('yearsLabel').style.display = 'none'; // Hide the years input
  document.getElementById('years').style.display = 'none'; // Hide the years input
});

// Function to generate a recommendation based on the month
function getRecommendation(month) {
  // Get the rainfall value for the selected month
  const rainfall = rainfallData[month];

  // If the rainfall is above 100mm, recommend against traveling that month
  if (rainfall > 100) {
    return `It might not be the best time to travel to Hong Kong in ${month} due to high rainfall. You can view more information about best months to visit Hong Kong on our "Travel Recommendation" page.`;
  } else {
    // Otherwise, suggest it's a good time to visit
    return `${month} is a great month to visit Hong Kong, with relatively low rainfall. You can view more information about best months to visit Hong Kong on our "Travel Recommendation" page.`;
  }
}

// Show the years input if the user chooses "Yes" for receiving data
document.querySelectorAll('input[name="receiveData"]').forEach(radio => {
  radio.addEventListener('change', function() {
    if (this.value === 'true') {
      document.getElementById('yearsLabel').style.display = 'block';
      document.getElementById('years').style.display = 'block';
    } else {
      document.getElementById('yearsLabel').style.display = 'none';
      document.getElementById('years').style.display = 'none';
    }
  });
});

