import React from 'react';
import ReactDOM from 'react-dom';

class Child extends React.Component{
    constructor(props){
        super(props)
    }
    handleClick(){
        this.setState({
            age: this.state.age + 1
        })
    }
    render(){
        return (
            <div>
                <h1>Father's background color: {this.props.bgColor}</h1>
                <button onClick={(e) => this.handleClick(e)}>chg father's background color</button>
            </div>
        )
    }
}

class Father extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            bgColor: '#999'
        }
    }
    render(props){
        return <Child bgColor={this.state.bgColor}/>
    }
}

ReactDOM.render(
    <Father/>,
    document.getElementById('root')
);