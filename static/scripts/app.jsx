import React from 'react';
import ReactDOM from 'react-dom';
import {BrowserRouter as Router, Route, Link, Switch} from 'react-router-dom';
//import element from './index.jsx';

class A extends React.Component{
    constructor(props){
        super(props)
    }
    render(){
        return (
            <div>
                Component A
                <Switch>
                    <Route exact path={`${this.props.match.path}`}
                    render={(route) => 
                        {
                        return <div>
                            Current component is A without params
                            </div>
                        }}/>
                    <Route path={`${this.props.match.path}/sub`}
                    render={(route) => 
                        {
                        return <div>
                            Current component is sub
                            </div>
                        }}/>
                    <Route path={`${this.props.match.path}/:id`}
                    render={(route) => 
                        {
                        return <div>
                            Current component is A with params, the params is: {route.match.params.id}
                            </div>
                        }}/>
                </Switch>
            </div>
        );
    }
}

class B extends React.Component{
    constructor(props){
        super(props)
    }
    render(){
        return <div>Component B</div>
    }
}

class Wrapper extends React.Component{
    constructor(props){
        super(props)
    }
    render(){
        return (
        <div>
            <Link to="/a">Com-A</Link>
            <br/>
            <Link to="/a/sub">/a/sub</Link>
            <br/>
            <Link to="/a/123">Com-A with params</Link>
            <br/>
            <Link to="/b">Com-B</Link>
            {this.props.children}
        </div>
        );
    }
}

ReactDOM.render(
    <Router>
        <Wrapper>
            <Route path="/a" component={A}/>
            <Route path="/b" component={B}/>
        </Wrapper>
    </Router>,
    document.getElementById('root')
);