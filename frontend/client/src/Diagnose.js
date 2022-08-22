import React, {useState, useEffect} from 'react';
import Togglebutton from './Togglebutton';
import './Diagnose.css'
import {Routes, Route, useNavigate} from 'react-router-dom';
import Predict from './Predict';

function Diagnose(){

    const [data, setData] = useState([{}]);
    var letter = ""
    var all = []
    const navigate = useNavigate();

    useEffect(() => {
        fetch('/sys').then(
            res => res.json()
        ).then(
            data => {
                setData(data)
                // console.log(data)
            }
        )  
    }, [])

    const diagnose=()=> {
        console.log("Done clicked");
        navigate("/prediction")
    };
   
    return (
        <div className='Diagnose-page'>
            <div className='Diagnose-header'> 
                <h1>Select Symptoms: </h1>
            </div>
            
            <div className='Diagnose-header'>

            
                {(typeof {data} === "undefined") ? (
                    <p> [Loading...]</p>
                ) : (
                    <div>
    
                        {data.map((item) => (
                            <>
                            {item ? 
                                <div>
                                {(letter !== item.toString()[0]) ? <h3>{item.toString()[0].toUpperCase()}</h3>  : ""}

                                {(letter !== item.toString()[0]) ? (
                                letter=item.toString()[0],
                                <Togglebutton name={item.toString()} category_same={false}/>
                               ) 
                                : <Togglebutton name={item.toString()} category_same={true}/> }
                               
                                </div>
                            : "" }
                            </>
                        ))}

                    </div>
                )}
                
            </div>
            
            <div className='Diagnose-header'>   
                <button onClick={diagnose}>Done</button> 
            </div>
            
        </div>
    );
};

export default Diagnose;