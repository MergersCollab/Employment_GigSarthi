import React from "react";
import "./f04.css";

function Feature04() {
  return (

  <div style={{ padding: "20px" }}>
    
    <h2>Data Awakening & Cleaning Engine</h2>

    <h3>Dataset Preview</h3>
    <table border="1">
      <thead>
        <tr>
          <th>Worker</th>
          <th>Earnings</th>
          <th>Jobs</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>1</td>
          <td>450</td>
          <td>20</td>
        </tr>
        <tr>
          <td>2</td>
          <td>600</td>
          <td>25</td>
        </tr>
      </tbody>
    </table>

    <h3>Schema Validation</h3>
    <ul>
      <li>✔ earnings_per_day → numeric</li>
      <li>✔ hours_worked → numeric</li>
      <li>✔ jobs_completed → numeric</li>
      <li>✔ rating → numeric</li>
    </ul>

    <h3>Cleaning Summary</h3>
    <p>Removed missing values, converted 'ten' to numeric, and removed invalid entries.</p>

    <h3>Missing Value Report</h3>
    <p>Rows with missing values were removed.</p>

    <h3>Before vs After</h3>
    <p>Before Cleaning: 43 rows</p>
    <p>After Cleaning: 30 rows</p>

  </div>
);
}

export default Feature04;