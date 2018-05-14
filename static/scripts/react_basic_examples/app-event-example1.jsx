import React from 'react';
import ReactDOM from 'react-dom';

class Component extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            name: 'test name',
            age: 18
        }
        this.handleClick = this.handleClick.bind(this)
    }
    handleClick(){
        this.setState({
            age: this.state.age + 1
        });
    }
    render(){
        return (
            <div>
                <h1>I am {this.state.name}</h1>
                <p>I am {this.state.age} years old</p>
                <button onClick={this.handleClick}>add a year</button>
            </div>
        )
    }
}

ReactDOM.render(
    <Component/>,
    document.getElementById('root')
);