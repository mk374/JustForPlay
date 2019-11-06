import React, {Component, Context} from 'react';
import { BrowserRouter as Link} from 'react-router-dom'

import AppContext  from "../AppContext";

class GroupLink extends React.Component{
    handleClick = () => {
        this.props.onHeaderClick(this.props.value);
    }
    render(){
        return(
            <Link onClick={this.handleClick}>{this.props.value}</Link>
        )
    }
}

// list out user groups
class GroupLinks extends React.Component{
    constructor(props){
        super(props);
        // console.log(typeof this.props.groups);
        // console.log('GROUP LINKS:');
        // console.log(this.props.groups);

        // this.grouplinks = Object.keys(this.props.groups).map((key) => 
        //      <li key={key}>{JSON.stringify(this.props.groups[key])}</li>
        //      <li>hello</li>
        // )
    }
    
    getUrl = (gid) => {
        //post to url
    }
    
    render(){
        // var {grouplinks} = this;
        return(
            // {grouplinks}
            <p>Hello</p>
        )
    }
}

export default GroupLinks;