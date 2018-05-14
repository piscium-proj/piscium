import React from 'react';
import ReactDOM from 'react-dom';

class Component extends React.Component{
    constructor(props){
        super(props);
    }
    render(){
        return <h1>I am {this.props.name}</h1>
    }
}

ReactDOM.render(
    <div>
        <Component name="example123"/>
    </div>,
    document.getElementById('root')
);