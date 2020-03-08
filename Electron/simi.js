const icon = document.querySelector('i.fa.fa-microphone');
let paragraph = document.createElement('p');
let container = document.querySelector('.text-box');

container.appendChild(paragraph);
const sound =document.querySelector('.sound');

window.SpeechRecognition = webkitSpeechRecognition || window.SpeechRecognition;
const synth = window.speechSynthesis;
recognition = new SpeechRecognition();
recognition.interimResults = true;

icon.addEventListener('click', () => {
	sound.play();
	dictate();
})

const dictate = () => {
	recognition.start();
	recognition.onresult = (event) => {
		const speechTotext = array.from(event.result)
		.map(result => result[0])
		.map(result => result.transcript)
		.join(' ');
		console.log(speechTotext);
		paragraph.textContent = speechTotext;
		if (event.result[0].isFinal) {
			paragraph = document.createElement('p');
			container.appendChild(paragraph);
			
			if(speechTotext.includes('what is the time')){
				speak(getTime);
			}
			if (speechTotext.includes('what is the date')) {
				speak(getDate);
			}
			if (speechTotext.includes('what is the weather in')) {
				getTheWeather(speechTotext);
			}
		}
	}
};

const speak = (action) => {
	const utterThis = new SpeechSynthesisUtterance(action());
	synth.speak(utterThis);
};

const getTime = () => {
	const time = new Date(Date.now())
	return `The time is ${time.toLocaleDateString('en_us', {hour: 'numeric', minute: 'numeric', hour12 : true})}`;
}

const getDate = () => {
	const time = new Date(Date.now())
	return `today is ${time.toLocaleDateString()}`;
}

const getTheWeather = (speech) => {
	fetch(`http://api.openweathermap.or/data/2.5/weather?q=${speech.split(' ')[5]}&appid=6aa90859f3e957ff6c77ec9b1bc86296&units=metric`)
	.then(function(response){
		return response.json();
	}).then(function(weather) {
		if (weather.cod === '404') {
			utterThis = new SpeechSynthesisUtterance(`I cannot find the weather for ${speech.split(' ')[5]}`);
			synth.speak(utterThis);
			return;
		}
		utterThis = new SpeechSynthesisUtterance(`The weathe condition in ${weather.name} is mostly mostly full of ${weather.weather[0].description} at a temperature of ${weather.main.temp} degrees celcius`);
		synth.speak(utterThis);
	})
}