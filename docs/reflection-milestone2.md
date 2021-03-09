# Milestone 2 Reflection

## General

The Board Game Analysis Dashboard is currently at a stage where it includes the functionality discussed in the proposal. However, it still requires layout and aesthetic optimization, additional in-app user documentation, and code clean-up/optimization to provide a polished product.

### Features Implemented

The current dashboard includes the following:

- Allows the user to select a category, mechanic, and or publisher and display counts of games and user ratings over the range of available published years.
- Provides bar charts that displays the top 5 categories, mechanics, and or publishers based on a selected year range. Two of these bar chart series are provided to allow a comparison of different periods.
- The user can filter on multiple selections of category, mechanic, publisher and date range and the the top 10 board games by user rating will be displayed graphically and in table format.

These features are implemented although there may changes as part of Milestone 4. Performance for the top two figures on the first tab will also need to be improved for Milestone 4.

### Additional Work

The following additional work will be completed on the dashboard to create a more polished product in Milestone 4:

- Updates to the layout and aesthetics of the dashboard. This includes adding space between sections of the dashboard and maximizing white space.
- Additional user instructions added to the application. This may include pop-ups and hover-overs as well as ensuring the app is easily understandable.
- The duplicated series of categorical ranking bar charts on the first tab may be merged into a single series of bar charts allowing side-by-side bar results, or an additional style of plot may be considered to replace this. The bar charts also currently have an issue of vertical scrolling due to the x-axis title names which will be fixed (although may be replaced by another chart type).

Code clean-up will also be required for the dashboard. Our team focused on implementing functionality during this milestone and it is recognized that an additional review of code should be completed. Github Issues [#34](https://github.com/ubco-mds-2020-labs/dashboard-project-group14/issues/34) and [#35](https://github.com/ubco-mds-2020-labs/dashboard-project-group14/issues/35) note some of the issues to be addressed in Milestone 4.

### Enhancements

In general, the functionality implemented performs well but it is recognized that it is somewhat basic (partially a function of the project timeline). The current dataset is also a few years out of date. The following enhancements are being pursued to address these.

- Implementing dimensionality reduction of the categories and mechanics into 2-dimensions to allow 3-dimensional plotting with user rating as the third axis. This will allow a user to visually explore similarities between board games. An analysis of this is provided in the reports folder and a framework app with the 3D interactive plot is provided [here](https://github.com/ubco-mds-2020-labs/dashboard-project-group14/blob/main/reports/tsne_analysis/). The analysis proved successful and the goal will be to implement the 3D plot in an additional tab.
- Updating the board game dataset. The original exploratory data analysis (EDA) was completed using a dataset that ended in 2016 and an updated and cleaned version of the dataset is not available. We are currently working on getting additional data to update the database. This is taking more effort than originally anticipated but is progressing.

Other enhancements originally considered included deploying the app through AWS and putting the database in NoSQL; however, these may not be completed based on the effort required for the enhancements currently underway.
