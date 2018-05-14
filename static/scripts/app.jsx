import React from 'react';
import ReactDOM from 'react-dom';
import {BrowserRouter as Router, Route, Link, Switch, Redirect} from 'react-router-dom';

import Home from 'scripts/home/index.jsx';
import ClassicLayout from 'scripts/src/component/layout/index.jsx';

class App extends React.Component{
    render(){
        return (
            <div>
                <Router>
                    <Switch>
                        <Route exact path="/" component={Home}/>
                        <Redirect from="*" to="/"/>
                    </Switch>
                </Router>
            </div>
        )
    }
}

ReactDOM.render(
    <ClassicLayout/>,
    document.getElementById('root')
);