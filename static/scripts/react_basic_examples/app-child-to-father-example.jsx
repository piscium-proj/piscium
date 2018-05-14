import React from 'react';
import ReactDOM from 'react-dom';

class Child extends React.Component{
    constructor(props){
        super(props)
    }
    handleClick(e){
        this.props.changeColor('red');
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
    onBgColorChange(color){
        this.setState({
            bgColor: color
        })
    }
    render(props){
        return (
            <div style={{background: this.state.bgColor}}>
                <Child bgColor={this.state.bgColor} changeColor={(color) => {this.onBgColorChange(color)}}/>
            </div>
        )
    }
}

ReactDOM.render(
    <Father/>,
    document.getElementById('root')
);