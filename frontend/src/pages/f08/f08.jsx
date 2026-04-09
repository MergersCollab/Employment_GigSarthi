import React from "react";
import "./f08.css";

function Feature08() {
  return (
    <div className="f08-container">

      <h2>Worker Intelligence Engine</h2>

      <h3>Stability Score Formula</h3>
      <p className="formula">
        Stability = (earnings_per_day + jobs_completed + rating) / hours_worked
      </p>

      <h3>Average Stability</h3>
      <p className="highlight">Average Stability Score: 72</p>

      <h3>Worker Segmentation Table</h3>
      <table className="f08-table">
        <thead>
          <tr>
            <th>Worker</th>
            <th>Stability</th>
            <th>Segment</th>
            <th>Risk</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>1</td>
            <td>56</td>
            <td>Cluster 0</td>
            <td>Low Risk</td>
          </tr>
          <tr>
            <td>2</td>
            <td>70</td>
            <td>Cluster 1</td>
            <td>Medium</td>
          </tr>
        </tbody>
      </table>

      <h3>Risk Meaning</h3>
      <ul className="f08-list">
        <li>High Risk → Low income, inconsistent work</li>
        <li>Medium → Moderate stability</li>
        <li>Stable → High income, consistent work</li>
      </ul>

      <h3>Worker Segmentation Graph</h3>
      <img src="/cluster_plot.png" className="graph" alt="Cluster Graph" />

      <h3>Cluster Distribution</h3>
      <img src="/cluster_distribution.png" className="graph" alt="Distribution Graph" />

      <h3>Insights</h3>
      <p className="insight">
        Most workers fall into moderate category, while a few high earners exist with fewer jobs.
      </p>

    </div>
  );
}

export default Feature08;