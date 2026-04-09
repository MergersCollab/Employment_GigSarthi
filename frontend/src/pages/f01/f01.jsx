import React, { useState } from "react";
import "./f01.css";

function Feature01() {
  const [loading, setLoading] = useState(false);
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  const runFeature = async () => {
    setLoading(true);
    setError(null);
    setData(null);
    
    try {
      const res = await fetch("http://localhost:5000/api/features/01");
      if (!res.ok) {
        throw new Error(`HTTP error! status: ${res.status}`);
      }
      const result = await res.json();
      setData(result);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="f01-container">
      <div className="f01-header">
        <h2 className="f01-title">Data Awakening</h2>
        <p className="f01-subtitle">
          Extract raw gig economy data dynamically from platforms like Freelancer and convert it into a structured, usable dataset.
        </p>
      </div>

      <button className="extract-btn" onClick={runFeature} disabled={loading}>
        {loading ? (
          <>
            <div className="spinner"></div> Extracting Data...
          </>
        ) : (
          "Initialize Platform Scraper"
        )}
      </button>

      {error && (
        <div className="status-message error">
          Failed to extract data: {error}
        </div>
      )}

      {data && (
        <div className={`status-message ${data.status === 'fallback' ? 'fallback' : ''}`}>
          {data.message}
        </div>
      )}

      {data && data.data && (
        <div className="jobs-grid">
          {data.data.map((job) => (
            <div className="job-card" key={job.id}>
              <h3 className="job-title">{job.title}</h3>
              <div className="job-price">{job.price}</div>
              <p className="job-desc">{job.description}</p>
              <div className="job-skills">
                {job.skills && job.skills.map((skill, index) => (
                  <span className="skill-tag" key={index}>{skill}</span>
                ))}
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default Feature01;