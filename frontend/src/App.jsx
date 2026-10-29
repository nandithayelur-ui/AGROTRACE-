import { useState, useEffect, useCallback } from 'react'
import './App.css'
import { agroApi } from './api.js'

// ── icons (inline SVG to avoid extra deps) ──────────────────────────────────
const Icon = ({ name, size = 16 }) => {
  const icons = {
    dashboard: (
      <svg width={size} height={size} viewBox="0 0 20 20" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round">
        <rect x="2" y="2" width="7" height="7" rx="1.5"/><rect x="11" y="2" width="7" height="7" rx="1.5"/>
        <rect x="2" y="11" width="7" height="7" rx="1.5"/><rect x="11" y="11" width="7" height="7" rx="1.5"/>
      </svg>
    ),
    lots: (
      <svg width={size} height={size} viewBox="0 0 20 20" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round">
        <path d="M4 4h12M4 8h8M4 12h10M4 16h6"/>
      </svg>
    ),
    quality: (
      <svg width={size} height={size} viewBox="0 0 20 20" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round">
        <path d="M4 10l4 4 8-8"/>
      </svg>
    ),
    warehouse: (
      <svg width={size} height={size} viewBox="0 0 20 20" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round">
        <path d="M2 18V9l8-6 8 6v9"/><path d="M8 18v-5h4v5"/>
      </svg>
    ),
    payments: (
      <svg width={size} height={size} viewBox="0 0 20 20" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round">
        <rect x="2" y="5" width="16" height="12" rx="2"/><path d="M2 9h16"/>
      </svg>
    ),
    quantum: (
      <svg width={size} height={size} viewBox="0 0 20 20" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round">
        <circle cx="10" cy="10" r="2"/><ellipse cx="10" cy="10" rx="8" ry="3.5"/>
        <ellipse cx="10" cy="10" rx="8" ry="3.5" transform="rotate(60 10 10)"/>
        <ellipse cx="10" cy="10" rx="8" ry="3.5" transform="rotate(120 10 10)"/>
      </svg>
    ),
    plus: (
      <svg width={size} height={size} viewBox="0 0 20 20" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round">
        <path d="M10 4v12M4 10h12"/>
      </svg>
    ),
    user: (
      <svg width={size} height={size} viewBox="0 0 20 20" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round">
        <circle cx="10" cy="7" r="3.5"/><path d="M2.5 18c0-4 3.4-7 7.5-7s7.5 3 7.5 7"/>
      </svg>
    ),
    arrow: (
      <svg width={size} height={size} viewBox="0 0 20 20" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
        <path d="M4 10h12M12 6l4 4-4 4"/>
      </svg>
    ),
    close: (
      <svg width={size} height={size} viewBox="0 0 20 20" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round">
        <path d="M5 5l10 10M15 5l-10 10"/>
      </svg>
    ),
    trend_up: (
      <svg width={size} height={size} viewBox="0 0 20 20" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
        <path d="M4 14l4-4 4 3 5-6"/><path d="M14 7h4v4"/>
      </svg>
    ),
    check: (
      <svg width={size} height={size} viewBox="0 0 20 20" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
        <path d="M4 10l4 4 8-8"/>
      </svg>
    ),
    clock: (
      <svg width={size} height={size} viewBox="0 0 20 20" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round">
        <circle cx="10" cy="10" r="8"/><path d="M10 6v4l3 2"/>
      </svg>
    ),
    leaf: (
      <svg width={size} height={size} viewBox="0 0 20 20" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round">
        <path d="M10 17s-8-3-7-11c4-1 8 1 10 5 0 0 2-6 5-6 1 5-3 9-8 12z"/>
      </svg>
    ),
    refresh: (
      <svg width={size} height={size} viewBox="0 0 20 20" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round">
        <path d="M4 10a6 6 0 0110.4-4.1"/><path d="M16 10a6 6 0 01-10.4 4.1"/>
        <path d="M14 5.9l.4-2L16 4.5"/><path d="M6 14.1l-.4 2L4 15.5"/>
      </svg>
    ),
  }
  return <span className="icon" aria-hidden="true">{icons[name] ?? null}</span>
}

// ── Tab config ───────────────────────────────────────────────────────────────
const TABS = [
  { id: 'Dashboard',            icon: 'dashboard' },
  { id: 'Lots',                 icon: 'lots'      },
  { id: 'Quality Grading',      icon: 'quality'   },
  { id: 'Warehouse Allocation', icon: 'warehouse' },
  { id: 'Payments',             icon: 'payments'  },
  { id: 'Quantum Runs',         icon: 'quantum'   },
]

const CROPS = ['Rice', 'Wheat', 'Tomatoes', 'Potatoes', 'Onions', 'Maize', 'Soybean']
const WAREHOUSES = ['Warehouse North', 'Warehouse Central', 'Warehouse South']

// ── Toast ────────────────────────────────────────────────────────────────────
function Toast({ toasts }) {
  return (
    <div className="toast-container">
      {toasts.map(t => (
        <div key={t.id} className={`toast toast-${t.type}`}>
          <Icon name={t.type === 'success' ? 'check' : 'clock'} size={14} />
          <span>{t.message}</span>
        </div>
      ))}
    </div>
  )
}

// ── Status badge ─────────────────────────────────────────────────────────────
function StatusBadge({ value }) {
  const isGood = value === 'Verified' || value === 'Settled' || value === 'Demo settled'
  return (
    <span className={`badge ${isGood ? 'badge-good' : 'badge-pending'}`}>
      <Icon name={isGood ? 'check' : 'clock'} size={11} />
      {value}
    </span>
  )
}

// ── Stat card ────────────────────────────────────────────────────────────────
function StatCard({ label, value, sub, icon, accent }) {
  return (
    <article className={`stat-card ${accent ? 'stat-card-accent' : ''}`}>
      <div className="stat-card-header">
        <span className="stat-label">{label}</span>
        <span className="stat-icon"><Icon name={icon} size={16} /></span>
      </div>
      <strong className="stat-value">{value}</strong>
      <small className="stat-sub">{sub}</small>
    </article>
  )
}

// ── Lot table ────────────────────────────────────────────────────────────────
function LotTable({ lots }) {
  if (!lots.length) {
    return <div className="empty-state"><Icon name="leaf" size={32} /><p>No lots registered yet.</p></div>
  }
  return (
    <div className="table-wrap">
      <table>
        <thead>
          <tr>
            <th>LOT ID</th><th>PRODUCE</th><th>QUANTITY</th><th>QUALITY</th><th>STATUS</th>
          </tr>
        </thead>
        <tbody>
          {lots.map(lot => (
            <tr key={lot.id}>
              <td><span className="lot-id">{lot.id}</span></td>
              <td>
                <span className="crop-cell">
                  <span className="crop-dot" />
                  {lot.crop}
                </span>
              </td>
              <td><span className="quantity-cell">{Number(lot.quantity).toLocaleString()} kg</span></td>
              <td><span className={`grade ${lot.grade === 'Pending' ? 'grade-pending' : 'grade-ok'}`}>{lot.grade}</span></td>
              <td><StatusBadge value={lot.status} /></td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}

// ── Register modal ───────────────────────────────────────────────────────────
function RegisterModal({ onClose, onSubmit }) {
  const [crop, setCrop] = useState('Rice')
  const [quantity, setQuantity] = useState('')
  const [grade, setGrade] = useState('Grade A')
  const [farmer, setFarmer] = useState('')
  const [loading, setLoading] = useState(false)

  async function handleSubmit(e) {
    e.preventDefault()
    if (!quantity || Number(quantity) <= 0) return
    setLoading(true)
    await onSubmit({ crop, quantity: Number(quantity), grade, farmer })
    setLoading(false)
  }

  return (
    <div className="modal-backdrop" onClick={e => e.target === e.currentTarget && onClose()}>
      <div className="modal">
        <div className="modal-header">
          <div>
            <p className="eyebrow">NEW AGRICULTURAL BATCH</p>
            <h2>Register produce</h2>
          </div>
          <button className="icon-btn" onClick={onClose} aria-label="Close"><Icon name="close" size={18} /></button>
        </div>

        <form onSubmit={handleSubmit}>
          <div className="form-grid">
            <label className="field">
              <span>Crop type</span>
              <select value={crop} onChange={e => setCrop(e.target.value)}>
                {CROPS.map(c => <option key={c}>{c}</option>)}
              </select>
            </label>
            <label className="field">
              <span>Quality grade</span>
              <select value={grade} onChange={e => setGrade(e.target.value)}>
                <option>Grade A</option>
                <option>Grade B</option>
                <option>Grade C</option>
                <option>Pending</option>
              </select>
            </label>
          </div>
          <label className="field">
            <span>Quantity (kg)</span>
            <input
              type="number" min="1" required
              value={quantity} onChange={e => setQuantity(e.target.value)}
              placeholder="e.g. 1 200"
            />
          </label>
          <label className="field">
            <span>Farmer / supplier name <em>(optional)</em></span>
            <input
              type="text"
              value={farmer} onChange={e => setFarmer(e.target.value)}
              placeholder="e.g. Ravi Shankar"
            />
          </label>
          <button className="primary-btn full-width" type="submit" disabled={loading}>
            {loading ? 'Registering…' : 'Register lot'}
          </button>
        </form>
      </div>
    </div>
  )
}

// ── Quantum panel ────────────────────────────────────────────────────────────
function QuantumPanel({ addToast }) {
  const [runs, setRuns] = useState([])
  const [loading, setLoading] = useState(false)

  const fetchRuns = useCallback(async () => {
    try {
      const data = await agroApi.getRuns()
      setRuns(Array.isArray(data) ? data : [])
    } catch {
      // silently fail - API may not be running
    }
  }, [])

  useEffect(() => { fetchRuns() }, [fetchRuns])

  async function runExperiment(experiment) {
    setLoading(true)
    try {
      await agroApi.runQuantum(experiment)
      addToast('Quantum experiment queued', 'success')
      setTimeout(fetchRuns, 1000)
    } catch {
      addToast('API not reachable - demo mode', 'info')
    } finally {
      setLoading(false)
    }
  }

  const experiments = ['bell_qrng', 'grover', 'qft', 'shor']

  return (
    <section className="panel">
      <div className="panel-heading">
        <div>
          <h3>Quantum experiment runs</h3>
          <p>QpiAI quantum circuit executions</p>
        </div>
        <button className="icon-btn-outline" onClick={fetchRuns} aria-label="Refresh">
          <Icon name="refresh" size={14} /> Refresh
        </button>
      </div>

      <div className="experiment-grid">
        {experiments.map(exp => (
          <button
            key={exp}
            className="experiment-card"
            onClick={() => runExperiment(exp)}
            disabled={loading}
          >
            <Icon name="quantum" size={22} />
            <span>{exp.replace('_', ' ')}</span>
          </button>
        ))}
      </div>

      {runs.length > 0 && (
        <div className="run-list">
          <p className="run-list-title">Recent runs</p>
          {runs.slice(0, 6).map((run, i) => (
            <div className="list-row" key={i}>
              <div>
                <strong>{run.experiment ?? `Run ${i + 1}`}</strong>
                <p>{run.status ?? 'completed'}</p>
              </div>
              <StatusBadge value={run.status === 'ok' ? 'Verified' : run.status ?? 'Verified'} />
            </div>
          ))}
        </div>
      )}

      {runs.length === 0 && (
        <div className="empty-state">
          <Icon name="quantum" size={30} />
          <p>No runs yet. Trigger an experiment above.</p>
        </div>
      )}
    </section>
  )
}

// ── Main App ─────────────────────────────────────────────────────────────────
function App() {
  const [activeTab, setActiveTab] = useState('Dashboard')
  const [lots, setLots] = useState([
    { id: 'LOT001', crop: 'Rice',     quantity: 2000, grade: 'Grade A', status: 'Verified',          farmer: 'Ravi Shankar'  },
    { id: 'LOT002', crop: 'Tomatoes', quantity:  800, grade: 'Pending', status: 'Inspection pending', farmer: 'Anita Patel'   },
    { id: 'LOT003', crop: 'Wheat',    quantity: 1500, grade: 'Grade B', status: 'Verified',          farmer: 'Suresh Kumar'  },
  ])
  const [showForm, setShowForm]   = useState(false)
  const [toasts,   setToasts]     = useState([])
  const [apiLots,  setApiLots]    = useState(null)

  useEffect(() => {
    agroApi.getLots().then(data => {
      if (Array.isArray(data) && data.length > 0) setApiLots(data)
    }).catch(() => {})
  }, [])

  const displayLots = apiLots ?? lots

  function addToast(message, type = 'success') {
    const id = Date.now()
    setToasts(prev => [...prev, { id, message, type }])
    setTimeout(() => setToasts(prev => prev.filter(t => t.id !== id)), 3500)
  }

  async function registerLot(data) {
    const newLot = {
      id: `LOT${String(lots.length + 1).padStart(3, '0')}`,
      ...data,
      status: 'Inspection pending',
    }
    setLots(prev => [...prev, newLot])
    setShowForm(false)
    setActiveTab('Lots')
    addToast(`Lot ${newLot.id} registered successfully`)
  }

  const totalQuantity = displayLots.reduce((sum, l) => sum + Number(l.quantity ?? 0), 0)
  const verified      = displayLots.filter(l => l.status === 'Verified').length
  const verifiedPct   = displayLots.length ? Math.round((verified / displayLots.length) * 100) : 0

  return (
    <div className="app">
      {/* Sidebar */}
      <aside className="sidebar">
        <div className="brand">
          <span className="brand-icon"><Icon name="leaf" size={20} /></span>
          AgriTrace
        </div>

        <p className="side-label">WORKSPACE</p>
        <nav>
          {TABS.map(tab => (
            <button
              key={tab.id}
              className={`nav-item ${activeTab === tab.id ? 'active' : ''}`}
              onClick={() => setActiveTab(tab.id)}
            >
              <Icon name={tab.icon} size={16} />
              <span>{tab.id}</span>
              {activeTab === tab.id && <span className="nav-active-bar" />}
            </button>
          ))}
        </nav>

        <div className="sidebar-footer">
          <p className="footer-tagline">Transparent trade.<br />Trusted records.</p>
          <div className="api-status">
            <span className={`dot ${apiLots ? 'dot-live' : 'dot-demo'}`} />
            {apiLots ? 'Live API' : 'Demo mode'}
          </div>
        </div>
      </aside>

      {/* Main content */}
      <main className="main">
        <header className="topbar">
          <div>
            <p className="eyebrow">AGRICULTURAL PROCUREMENT PLATFORM</p>
            <h1>{activeTab}</h1>
          </div>
          <div className="topbar-right">
            {(activeTab === 'Dashboard' || activeTab === 'Lots') && (
              <button className="primary-btn" onClick={() => setShowForm(true)}>
                <Icon name="plus" size={14} /> Register produce
              </button>
            )}
            <div className="profile">
              <span className="avatar"><Icon name="user" size={18} /></span>
              <div className="profile-text">
                <strong>Demo User</strong>
                <small>Project workspace</small>
              </div>
            </div>
          </div>
        </header>

        {/* Dashboard */}
        {activeTab === 'Dashboard' && (
          <>
            <section className="welcome">
              <div className="welcome-content">
                <p className="eyebrow light">AGRICULTURE · TRANSPARENCY · TRUST</p>
                <h2>Procurement, made clearer.</h2>
                <p>Track produce, verify quality and monitor settlements in one transparent platform.</p>
                <div className="welcome-actions">
                  <button className="primary-btn white" onClick={() => setShowForm(true)}>
                    <Icon name="plus" size={14} /> Register produce
                  </button>
                  <button className="outline-btn white" onClick={() => setActiveTab('Lots')}>
                    View all lots <Icon name="arrow" size={14} />
                  </button>
                </div>
              </div>
              <div className="welcome-illustration">
                <div className="welcome-circle">🌾</div>
              </div>
            </section>

            <div className="stats">
              <StatCard label="Total lots"       value={displayLots.length}                        sub="Registered batches"          icon="lots"      />
              <StatCard label="Quantity tracked" value={`${totalQuantity.toLocaleString()} kg`}   sub="Across all lots"             icon="trend_up"  />
              <StatCard label="Quality verified" value={`${verified} / ${displayLots.length}`}    sub={`${verifiedPct}% pass rate`} icon="quality"   accent />
              <StatCard label="Payments pending" value="3"                                         sub="Awaiting settlement"         icon="payments"  />
            </div>

            <div className="progress-banner">
              <div className="progress-info">
                <span>Verification progress</span>
                <strong>{verifiedPct}%</strong>
              </div>
              <div className="progress-track">
                <div className="progress-fill" style={{ width: `${verifiedPct}%` }} />
              </div>
            </div>

            <section className="panel">
              <div className="panel-heading">
                <div>
                  <h3>Recent produce lots</h3>
                  <p>Overview of registered agricultural batches</p>
                </div>
                <button className="text-btn" onClick={() => setActiveTab('Lots')}>
                  View all <Icon name="arrow" size={13} />
                </button>
              </div>
              <LotTable lots={displayLots.slice(0, 4)} />
            </section>
          </>
        )}

        {/* Lots */}
        {activeTab === 'Lots' && (
          <section className="panel">
            <div className="panel-heading">
              <div>
                <h3>Produce inventory</h3>
                <p>Track batches from registration onward</p>
              </div>
              <button className="primary-btn" onClick={() => setShowForm(true)}>
                <Icon name="plus" size={14} /> Register produce
              </button>
            </div>
            <LotTable lots={displayLots} />
          </section>
        )}

        {/* Quality Grading */}
        {activeTab === 'Quality Grading' && (
          <section className="panel">
            <div className="panel-heading">
              <div>
                <h3>Quality inspection</h3>
                <p>Demo records - no real inspector connected</p>
              </div>
            </div>
            <div className="list-body">
              {displayLots.map(lot => (
                <div className="list-row" key={lot.id}>
                  <div className="list-row-main">
                    <span className="crop-dot" />
                    <div>
                      <strong>{lot.crop} · {lot.id}</strong>
                      <p>{Number(lot.quantity).toLocaleString()} kg{lot.farmer ? ` · ${lot.farmer}` : ''}</p>
                    </div>
                  </div>
                  <div className="list-row-actions">
                    <span className={`grade ${lot.grade === 'Pending' ? 'grade-pending' : 'grade-ok'}`}>{lot.grade}</span>
                    <StatusBadge value={lot.status} />
                  </div>
                </div>
              ))}
            </div>
          </section>
        )}

        {/* Warehouse Allocation */}
        {activeTab === 'Warehouse Allocation' && (
          <section className="panel">
            <div className="panel-heading">
              <div>
                <h3>Warehouse allocation</h3>
                <p>Sample allocation preview - QpiAI Opt integration available</p>
              </div>
              <button
                className="outline-btn"
                onClick={async () => {
                  try {
                    await agroApi.optimizeAllocation('exact', false)
                    addToast('Allocation optimised', 'success')
                  } catch {
                    addToast('Using demo allocation', 'info')
                  }
                }}
              >
                Run optimizer
              </button>
            </div>
            <div className="list-body">
              {displayLots.map((lot, index) => (
                <div className="list-row" key={lot.id}>
                  <div className="list-row-main">
                    <div className="warehouse-icon"><Icon name="warehouse" size={16} /></div>
                    <div>
                      <strong>{lot.crop} · {lot.id}</strong>
                      <p>{Number(lot.quantity).toLocaleString()} kg available</p>
                    </div>
                  </div>
                  <div className="warehouse-chip">
                    <Icon name="warehouse" size={12} />
                    {WAREHOUSES[index % 3]}
                  </div>
                </div>
              ))}
            </div>
          </section>
        )}

        {/* Payments */}
        {activeTab === 'Payments' && (
          <section className="panel">
            <div className="panel-heading">
              <div>
                <h3>Payment tracking</h3>
                <p>Illustrative statuses - no real payments processed</p>
              </div>
            </div>
            <div className="list-body">
              {displayLots.map((lot, index) => (
                <div className="list-row" key={lot.id}>
                  <div className="list-row-main">
                    <div className={`payment-avatar ${index === 0 ? 'payment-settled' : 'payment-pending'}`}>
                      <Icon name="payments" size={14} />
                    </div>
                    <div>
                      <strong>{lot.id} · {lot.crop}</strong>
                      <p>Qty: {Number(lot.quantity).toLocaleString()} kg{lot.farmer ? ` · ${lot.farmer}` : ''}</p>
                    </div>
                  </div>
                  <div className="payment-amount">
                    <span className="amount">&#x20B9;{(Number(lot.quantity) * (lot.grade === 'Grade A' ? 28 : 22)).toLocaleString()}</span>
                    <StatusBadge value={index === 0 ? 'Settled' : 'Inspection pending'} />
                  </div>
                </div>
              ))}
            </div>
          </section>
        )}

        {/* Quantum Runs */}
        {activeTab === 'Quantum Runs' && (
          <QuantumPanel addToast={addToast} />
        )}

        <footer>
          AgriTrace · Hackathon prototype · {apiLots ? 'Live data' : 'Sample data only'}
        </footer>
      </main>

      {showForm && (
        <RegisterModal onClose={() => setShowForm(false)} onSubmit={registerLot} />
      )}

      <Toast toasts={toasts} />
    </div>
  )
}

export default App
