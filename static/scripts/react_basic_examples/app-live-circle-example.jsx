import React from 'react';
import ReactDOM from 'react-dom';

class Component extends React.Component{
    //contructor function
    constructor(props){
        super(props)
        this.state = {
            data: 'Old props'
        }
        console.log('initial data','constractor')
    }
    //component will mount
    //here code sync methods
    componentWillMount(){
        console.log('componentWillMount')
    }
    //component did mount
    componentDidMount(){ 
        console.log('componentDidMount')
    }
    //component will reveice father's props
    componentWillReceiveProps(){
        console.log('componentWillReceiveProps')
    }
     //if component child should be updated
    shouldComponentUpdate(){
        console.log('shouldComponentUpdate');
        return true;
    }
    //component will update
    componentWillUpdate(){
        console.log('componentWillUpdate')
    }
    //componet did update
    componentDidUpdate(){
        console.log('componentDidUpdate')
    }
    //component will unmount
    componentWillUnmount(){
        console.log('componentWillUnmount')
    }
    //resolve click event
    handleClick(){
        console.log('here is updated data:')
        this.setState({
            data: 'New state'
        })
    }
    //render
    render(){
        console.log('render')
        return (
            <div>
                <div>Props: {this.props.data}</div>
                <button onClick={() => {this.handleClick()}}>
                Update component
                </button>
            </div>
        )
    }
}

class FatherComponent extends React.Component{
    //contructor function
    constructor(props){
        super(props)
        this.state = {
            data: 'Old props',
            hasChild: true
        }
        console.log('initial data','constractor')
    }
    onPropsChange(){
        console.log('update props:')
        this.setState({
            data: 'New props'
        })
    }
    onDestroyChild(){
        console.log('destory child')
        this.setState({
            hasChild: false
        })
    }
    render(){
        return (
            <div>
                {
                    this.state.hasChild ? <Component data={this.state.data}/> : null
                }
                <button onClick={() => {this.onPropsChange()}}>
                    change props
                </button>
                <button onClick={() => {this.onDestroyChild()}}>
                    destroy child component
                </button>
            </div>
        )
    }
}

ReactDOM.render(
    <FatherComponent/>,
    document.getElementById('root')
);