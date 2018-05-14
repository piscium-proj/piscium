import React from 'react';
import ReactDOM from 'react-dom';

class Child1 extends React.Component{
    constructor(props){
        super(props)
    }
    handleClick(e){
        this.props.changeChild2Color('red');
    }
    render(){
        return (
            <div>
                <h1>Child 1</h1>
                <button onClick={(e) => this.handleClick(e)}>chg Child2's background color</button>
            </div>
        )
    }
}

class Child2 extends React.Component{
    constructor(props){
        super(props)
    }
    render(){
        return (
            <div style={{background: this.props.bgColor}}>
                <h1>Child 2 background color: {this.props.bgColor}</h1>
            </div>
        )
    }
}

class Father extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            child2bgColor: '#999'
        }
    }
    onChild2BgColorChange(color){
        this.setState({
            child2bgColor: color
        })
    }
    render(props){
        return (
            <div>
                <Child1 changeChild2Color={(color) => {this.onChild2BgColorChange(color)}}/>
                <Child2 bgColor={this.state.child2bgColor}/>
            </div>
        )
    }
}

ReactDOM.render(
    <Father/>,
    document.getElementById('root')
);