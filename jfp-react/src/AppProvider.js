import React, {Component} from 'react';

import AppContext from './AppContext'

class AppProvider extends Component {
    state = {
         user: {test : 'test'},
         groups: ['Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5']
    };
    
    render() {
        return (
            <AppContext.Provider value={{user : this.state.user, groups : this.state.groups}}>
                {this.props.children}
            </AppContext.Provider>
        );
    }
}
export default AppProvider;