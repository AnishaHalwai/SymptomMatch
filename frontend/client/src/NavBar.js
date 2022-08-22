import React from 'react';
import { isCompositeComponentWithType } from 'react-dom/test-utils';
import {Link} from 'react-router-dom';

function NavBar(){
    return(
        <div>
            <Link to="/diagnose" style={{color: 'white'}}>Diagnose</Link>
        </div>
    );
}


export default NavBar;