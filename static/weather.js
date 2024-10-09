const apiKey = "539480bea5b24d478c575742242509";
const locationInput = document.getElementById("locationInput");
const searchButton = document.getElementById("searchButton");
const locationElement = document.getElementById("location");
const temperatureElement = document.getElementById("temperature");
const detail = document.querySelector(".weather-info");

const icon = document.querySelector(".icon");
// const descriptionElement = document.getElementById("description");

searchButton.addEventListener("click", () => {
  const location = locationInput.value.trim();
  detail.style.display = "none";
  if (location) {
    fetchWeather(location);

  } else {
    alert("Please enter a location");
  }
});

async function fetchWeather(location) {
  const url = `http://api.weatherapi.com/v1/current.json?key=${apiKey}&q=${location}&aqi=yes`;
  const a = await fetch(url);
  const response = await a.json();
  console.log(response);
  console.log(response.location.name);
  console.log(response.location.region);
  console.log(response.current.condition.icon.replace("//",""));
  console.log(response.current.temp_c);
  console.log(response.current.wind_mph);
  console.log(response.current.humidity);
  if(response.location.region == "Gujarat"){
    locationElement.textContent = response.location.name;
    temperatureElement.textContent = `${Math.round(response.current.temp_c)}°C`;
    icon.src = response.current.condition.icon;
    detail.style.display = "block";
  }else{
    alert("this city not in gujarat");
  }

}

