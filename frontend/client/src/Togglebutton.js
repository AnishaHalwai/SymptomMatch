import React, {useState} from 'react'
import './Togglebutton.css';



const Togglebutton = ({name, category_same}) => {
    const [selected, setSelected] = useState(false);
    const toggle=()=> {
        setSelected(!selected);
        if (!selected) {
            fetch("http://localhost:5000/diag", {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({"selected" : name})
                })
        }
        else{
            fetch("http://localhost:5000/diag", {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({"unselected" : name})
                })
        }
    }
    return (
        <div>
            {(category_same ? 
                <button onClick={toggle} className={(selected ? "toggle-select " + "same-category ": "toggle-unselect " + "same-category ")}>
                    {name}
                </button> : (
                <button onClick={toggle} className={(selected ? "toggle-select " + "diff-category ": "toggle-unselect " + "diff-category ")}>
                    {name}
                </button>)
             )}
            
            
        </div>
    )
}

export default Togglebutton