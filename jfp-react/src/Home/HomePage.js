import React from 'react';
import GroupLinks from './Groups';

class HomePage extends React.Component{
    render(){
        return(
            <GroupLinks groups={this.props.groups}/>
        );
    }
}
export default HomePage;