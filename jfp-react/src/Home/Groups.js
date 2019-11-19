import React from 'react';
import { BrowserRouter as Link} from 'react-router-dom'


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