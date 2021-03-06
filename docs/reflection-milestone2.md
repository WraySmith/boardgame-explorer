# Milestone 2 Reflection

## General

The Board Game Analysis Dashboard is currently at a stage where it includes the functionality indicated in the proposal. However, it still requires layout and aesthetic optimization, additional in-app user documentation, and code clean-up to provide a polished product.

### Features Implemented

The current dashboard includes the following:

- Allows the user to select a category, mechanic, and or publisher and display counts of games and user ratings from 1950 to 2021.
- Provides bar charts that displays the top 5 categories, mechanics, and or publishers based on a selected year range. Two of these bar chart series are provided to allow a comparison of different periods.
- The user can select a category, mechanic, or publisher as well a filter based on a date range the the top board games by user rating will be displayed graphically and in table format.

These features perform well although there may be minor changes (such as changes to filtering or selection logic) implemented as part of Milestone 4.

### Additional Work

The following additional work will be completed on the dashboard to create a more polished product in Milestone 4:

- Updates to the layout and aesthetics of the dashboard. This may include using more bootstrap features such as pop-ups or hover instructions.
- Additional user instructions added to the application. The current instructions are considered bare bones and additional time will be spent on UX considerations.
- The duplicated series of categorical ranking bar charts on the first tab may be merged into a single series of bar charts allowing side-by-side bar results.

Code clean-up will also be required for the dashboard. Our team focused on implementing functionality during this milestone and it is recognized that an additional review of code should be completed.

### Enhancements

In general, the functionality implemented performs well but it is recognized that it is somewhat basic (partially a function of the project timeline). The current dataset is also a few years out of date. The following enhancements are being pursued to address this.

- Implementing dimensionality reduction of the categories and mechanics into 2-dimensions to allow 3-dimensional plotting with user rating as the third axis. This will allow a user to visually explore similarities between board games. An analysis of this is provided in the reports folder and a framework app with the 3D interactive plot is provided here. The analysis proved successful and the goal will be to implement the 3D plot in an additional tab.
- Updating the board game dataset. The original exploratory data analysis (EDA) was completed using a dataset that ended in 2016 and an updated and cleaned version of the dataset is not available. We are currently working on getting additional data to update the database. This is taking more effort than originally anticipated but is progressing.

Other enhancements originally considered included deploying the app through AWS and putting the database in NoSQL; however, these may not be completed based on the effort required for the enhancements currently underway.
