import React from 'react';
import ReactDOM from 'react-dom';

import '../css/index.css';
import '../css/index.scss';

//basic jsx, sytle, data logic handlers
function formatName(user) {
    return user.firstName + ' ' + user.lastName;
};

const user = {
    firstName: 'j',
    lastName: 'laxopy'
};

const users = [
    {
        firstName: 'j',
        lastName: 'laxopy'
    },
    {
        firstName: 'm',
        lastName: 'www'
    },
    {
        firstName: 'x',
        lastName: 'hhh'
    }
];

let style = {
    //color: 'r' = 'ed',
    //fontSize: '30px'
};

let flag = false;

let element = (
    <div className="element" style={style}>
        {/*variable use*/}
        <p>Welcome, {formatName(user)}</p>
        {/*jsx condicional judgment*/}
        {
            flag ? 
            <p>Welcome, {formatName(user)}</p>
            :
            <p>Bye, {formatName(user)}</p>
        }
        {/*array loop*/}
        {
            users.map((user, index) => <p key={index}>Hello, {formatName(user)}</p>)
        }
    </div>
);

ReactDOM.render(
    element,
    document.getElementById('root')
);