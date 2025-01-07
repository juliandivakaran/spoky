import React, { useState, useEffect } from 'react';
import SpeechRecognition, { useSpeechRecognition } from 'react-speech-recognition'
//import { useSpeechRecognition } from 'react-speech-recognition';

function App() {
    //const { listening, resetTranscript } = useSpeechRecognition();
    //setting up for speach recognitation
    const { listening, resetTranscript, transcript } = useSpeechRecognition(); // Moved inside function
    const handleSpeechSubmit =() =>{
            fetch('http://127.0.0.1:8000/english/voiceAI/',{
                method:'POST',
                headers:{
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({voice:transcript}),
            })
            .then(response => response.json())
            .then(data => console.log(data))  // Log the response from the server
            .catch(error => console.error('Error:', error));
    const Dictaphone = () =>{
        const {
            transcript,
            listening,
            resetTranscript,
            browserSupportSpeechRecognition
        } = useSpeechRecognition();
        if (!browserSupportSpeechRecognition){
            return <span>Browser doesn't support speech recognition.</span>
        }



        }
    }

    //getting simple message from django backend
    const [message, setMessage] = useState('');

    useEffect(() => {
        fetch('http://localhost:8000/english/hello/')
            .then(response => response.json())
            .then(data => setMessage(data.message));
    }, []);

    //html body desining
    return (
        <div className="App">
            <p>Microphone: {listening ? 'on' : 'off'}</p>
            <button onClick={() =>SpeechRecognition.startListening()}>start</button>
            <button onClick={()=>SpeechRecognition.stopListening()}>stop</button>
            <button onClick={resetTranscript}>Reset</button>

            <h3>Transcript</h3>
            <p>{transcript}</p>
            <button onClick={handleSpeechSubmit}>submit</button>

            <h1>{message}</h1>
        </div>
    );
}

export default App;
