import React from 'react';
import ReactDOM from 'react-dom';

class Component extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            name : 'lalala'
        }
    }
    render(){
        setTimeout(() => {
            this.setState({
                name: 'change state with tiemout Test'
            })
        }, 2000)
        return <h1>I am {this.state.name}</h1>
    }
}

ReactDOM.render(
    <div>
        <Component/>
    </div>,
    document.getElementById('root')
);