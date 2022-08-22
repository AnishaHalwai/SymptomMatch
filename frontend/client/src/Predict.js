import React, {useState, useEffect} from 'react';
import Togglebutton from './Togglebutton';
import {Routes, Route} from 'react-router-dom';
import "./Predict.css"

function Predict(){
    const [data, setData] = useState([]);

    useEffect(() => {
        fetch('/predictions').then(
            res => res.json()
        ).then(
            data => {
                setData(data)
                console.log(data)
            }
        )  
    }, [])

    return (
        <div className="Predict-page">
            <div className='Predict-header'> 
                <h1>Your diagnosis: </h1>
            </div>
            {(typeof {data} === "undefined") ? (
                    <p> Loading...</p>
                ) : (
                <div>

                    {data.map((item) => (
                        <>
                        <h3>{item.toString()}</h3>
                        </>
                    ))}

                </div>
            )}
            
        </div>
    )
}

export default Predict;