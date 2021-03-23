# Milestone 4 Reflection

## General

The Board Game Analysis Dashboard includes the functionality originally proposed and incorporates the feedback after Milestone 2. We were also able to implement the two enhancements that were started during Milestone 2.

### Updates from Milestone 2

The following updates were made to the app building on top of Milestone 2 [feedback](https://github.com/ubco-mds-2020-labs/dashboard-project-group14/issues/34):

- Added user instructions and descriptions.
- Removed whitespace and tidied up app layout.
- Modified graph aesthetics.
- Modified the bar charts that previously existed in v0.1.1 of the app to be density plots. We felt this conveyed additional information not captured in the original bar charts. We also removed the duplicate set of charts which was originally envisioned to provide comparison but was ultimately felt to be not useful.

Several code based updates were also [completed](https://github.com/ubco-mds-2020-labs/dashboard-project-group14/issues/34) including:

- Vectorizing most wrangling operations to improve app speed (originally completed as part of the R app for Milestone 3 and then also completed here).
- Identifying and removing duplicated code ([jscpd](https://github.com/kucherenko/jscpd) was used as part of our super-linter process for this).
- Fixing a regex issue.

The app speed is now much better than it was during Milestone 2 and the current speed limitation is likely a function of the free hosting on Heroku.

The one item that did not get completed due to time constraints was modifying the top figure on the first tab (user rating vs published year). We feel that this graph could be improved but it would require additional effort to do so. For example, the graph could allow a user to toggle off points and provide an average line for each selection instead. This has been added to an open issue [here](https://github.com/ubco-mds-2020-labs/dashboard-project-group14/issues/69).

## Enhancements Added

We were also able to implement the two enhancement started during Milestone 2 including:

- Implementing dimensionality reduction (using t-SNE) of the categories and mechanics into 2-dimensions to allow 3-dimensional plotting with user rating as the third axis. This allows a user to visually explore similarities between board games. We found that the functionality of this works quite well providing a useful tool.
- Updating the board game dataset. The original exploratory data analysis (EDA) was completed using a dataset that ended in 2016 and the format/source of that data is no longer available. It was a significant amount of effort to update the dataset to 2021 but it was completed.

### Future Potential Enhancements

Other enhancements originally considered included deploying the app through AWS and putting the database in NoSQL which may improve the performance of the app.These were not be completed based on the effort required for the completed enhancements discussed above, but are potential future updates and are left as open [issues](https://github.com/ubco-mds-2020-labs/dashboard-project-group14/issues).
