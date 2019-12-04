import React from 'react';
import GroupLink from './GroupLink';

class HomePage extends React.Component{
    constructor(props){
        super(props);
        this.state={
            groups: this.props.groups
        }
    }

    render(){
        var groupLinks = this.state.groups;
        var groupLinksArr = [];
        groupLinks.forEach(group => {
            groupLinksArr.push(<GroupLink linkto= {group.communityid} name={group.group_name}></GroupLink>);
        });

        return(
            <div> 
                 <h1> MY GROUPS </h1>
                <div> 
                    {groupLinksArr}
                </div>
            </div>

        );
    }
}
export default HomePage;