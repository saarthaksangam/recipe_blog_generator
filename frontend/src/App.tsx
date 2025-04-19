import { useState, useEffect } from 'react';
import ReactMarkdown from 'react-markdown';
import rehypeRaw from 'rehype-raw';
import { motion, AnimatePresence } from 'framer-motion';
import './markdown-styles.css';
import './animations.css';

// Import icons
import { FaYoutube, FaCopy, FaCheck, FaCog, FaMarkdown } from 'react-icons/fa';
import { HiSparkles, HiOutlineDocumentText } from 'react-icons/hi';

interface BlogData {
  title: string;
  markdown: string;
  upload_date: string;
  thumbnail_url: string;
  youtube_url: string;
}

const loadingMessages = [
  "Extracting video details...",
  "Processing video transcript...",
  "Extracting subtitles...",
  "Extracting thumbnail...",
  "Generating recipe format...",
  "Creating blog structure...",
  "Applying cooking expertise...",
  "Adding flavor to the content...",
  "Finalizing your recipe blog...",
  "Almost ready to serve..."
];

function App() {
  const [youtubeUrl, setYoutubeUrl] = useState<string>('');
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);
  const [blogData, setBlogData] = useState<BlogData | null>(null);
  const [activeTab, setActiveTab] = useState<'preview' | 'markdown'>('preview');
  const [copySuccess, setCopySuccess] = useState<boolean>(false);
  const [loadingMessage, setLoadingMessage] = useState<string>(loadingMessages[0]);
  const [loadingProgress, setLoadingProgress] = useState<number>(0);

  // Extract YouTube embed URL
  const getYoutubeEmbedUrl = (url: string) => {
    const regExp = /^.*((youtu.be\/)|(v\/)|(\/u\/\w\/)|(embed\/)|(watch\?))\??v?=?([^#&?]*).*/;
    const match = url.match(regExp);
    const id = (match && match[7].length === 11) ? match[7] : '';
    return `https://www.youtube.com/embed/${id}?enablejsapi=1`;
  };

  useEffect(() => {
    if (!isLoading) return;
    let index = 0;
    let prog = 0;
    let errorShown = false;
    const start = Date.now();
    setLoadingMessage(loadingMessages[0]);

    const msgInterval = setInterval(() => {
      const elapsed = Date.now() - start;
      if (elapsed > 45000 && !errorShown) {
        setLoadingMessage("Server might be busy. Hang tight...");
        errorShown = true;
        return;
      }
      if (errorShown) return;
      index = Math.min(index + 1, loadingMessages.length - 1);
      setLoadingMessage(loadingMessages[index]);
      if (index === loadingMessages.length - 1) clearInterval(msgInterval);
    }, 1600);

    const progInterval = setInterval(() => {
      const inc = 95 - prog > 50 ? 5 : 95 - prog > 20 ? 3 : 1;
      prog = Math.min(prog + inc, 95);
      setLoadingProgress(prog);
    }, 800);

    return () => {
      clearInterval(msgInterval);
      clearInterval(progInterval);
      setLoadingProgress(0);
    };
  }, [isLoading]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!youtubeUrl.includes('youtube.com/') && !youtubeUrl.includes('youtu.be/')) {
      setError('Please enter a valid YouTube URL');
      return;
    }
    try {
      setIsLoading(true);
      setError(null);
      const res = await fetch(`http://localhost:8000/api/v1/generate-blog?youtube_url=${encodeURIComponent(youtubeUrl)}`);
      if (!res.ok) throw new Error((await res.json()).detail || 'Failed to generate blog');
      const data = await res.json();
      setBlogData(data);
      setLoadingProgress(100);
      setTimeout(() => setIsLoading(false), 500);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Unknown error');
      setIsLoading(false);
    }
  };

  const copyToClipboard = () => {
    if (!blogData) return;
    navigator.clipboard.writeText(blogData.markdown)
      .then(() => { setCopySuccess(true); setTimeout(() => setCopySuccess(false), 2000); })
      .catch(console.error);
  };

  const components = {
    img: ({ node, ...props }: any) => (
      <motion.img initial={{ opacity: 0, scale: 0.95 }} animate={{ opacity: 1, scale: 1 }} transition={{ duration: 0.5 }} {...props} className="markdown-image" />
    ),
    iframe: ({ node, ...props }: any) => {
      if (props.src?.includes('youtube.com')) {
        const src = props.src.includes('/embed/') ? props.src : getYoutubeEmbedUrl(props.src);
        return <div className="youtube-iframe-container"><iframe {...props} src={src} frameBorder="0" allowFullScreen className="youtube-iframe" /></div>;
      }
      return <iframe {...props} />;
    },
    blockquote: ({ node, ...props }: any) => {
      let text = '';
      node.children?.forEach((c: any) => c.children?.forEach((n: any) => n.value && (text += n.value)));
      text = text.replace(/^"|"$/g, '');
      if (/Posted on Youtube|By |Recipes that impress/.test(text)) {
        return (
          <motion.blockquote initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.5 }} className="metadata-blockquote">
            {text.includes('Posted on Youtube') && <p><FaYoutube className="inline-icon" />Posted {text.match(/on (\d{4}-\d{2}-\d{2})/)?.[1]}</p>}
            {text.includes('By ') && <p>By {text.match(/By ([^R]+)/)?.[1].trim()}</p>}
            {text.includes('Recipes that') && <p><span className="tagline">Recipes that impress with ease</span></p>}
          </motion.blockquote>
        );
      }
      return <blockquote {...props} />;
    }
  };

  return (
    <div className="app-container">
      <div className="main-content">
        <motion.header className="app-header" initial={{ opacity: 0, y: -20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.5 }}>
          <div className="header-content">
            <h1><HiSparkles className="title-icon" /> Recipe Blog Generator</h1>
            <p className="subtitle">Transform YouTube cooking videos into delicious blog posts</p>
          </div>
        </motion.header>

        {/* SPLIT HERO WITH BUILT-IN FORM & MOCK PREVIEW */}
        <motion.section className="hero-split" initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.6 }}>
          <div className="hero-left">
            <h2 className="hero-title">Turn Any Cooking Video into a Blog in Seconds</h2>
            <p className="hero-subtitle">Paste a YouTube link below and our AI will do the heavy lifting—ingredients, steps, tips, all formatted.</p>
            <form onSubmit={handleSubmit} className="hero-form">
              <div className="input-icon-wrapper">
                <FaYoutube className="input-icon" />
                <input type="url" value={youtubeUrl} onChange={e => setYoutubeUrl(e.target.value)} placeholder="Paste YouTube URL here..." className="url-input" required />
              </div>
              <button type="submit" className="submit-button" disabled={isLoading}>{isLoading ? 'Processing...' : 'Generate Blog'}</button>
            </form>
            {error && <motion.div className="error-message" initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }}>{error}</motion.div>}
          </div>

          <div className="hero-right">
            <div className="preview-mock">
              <div className="mock-header">Preview</div>
              <div className="mock-body">
                <h3>⭐ Grandma’s Best Apple Pie</h3>
                <ul>
                  <li>• 3 cups sliced apples</li>
                  <li>• 2 tbsp sugar</li>
                  <li>• 1 tsp cinnamon</li>
                </ul>
                <p>Preheat oven to 375°F. Toss apples with sugar & cinnamon…</p>
              </div>
            </div>
          </div>
        </motion.section>

        {/* RESULTS & LOADING */}
        <AnimatePresence>
          {isLoading && (
            <motion.div className="loading-container" initial={{ opacity: 0, scale: 0.95 }} animate={{ opacity: 1, scale: 1 }} exit={{ opacity: 0, scale: 0.9 }} transition={{ duration: 0.3 }}>
              <div className="loader-content">
                <div className="spinner-container"><div className="spinner"><FaCog className="spinner-icon" /></div></div>
                <div className="loading-text-container">
                  <motion.h3 className="loading-message" key={loadingMessage} initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} exit={{ opacity: 0, y: -10 }} transition={{ duration: 0.5 }}>{loadingMessage}</motion.h3>
                  <div className="progress-bar-container"><div className="progress-bar" style={{ width: `${loadingProgress}%` }} /></div>
                </div>
              </div>
            </motion.div>
          )}

          {blogData && !isLoading && (
              <motion.div className="result-container" initial={{opacity: 0, y: 20}} animate={{opacity: 1, y: 0}}
                          transition={{duration: 0.5}}>

                <div className="tabs">
                  <button onClick={() => setActiveTab('preview')}
                          className={`tab ${activeTab === 'preview' ? 'active' : ''}`}><HiOutlineDocumentText
                      className="tab-icon"/> Preview
                  </button>
                  <button onClick={() => setActiveTab('markdown')}
                          className={`tab ${activeTab === 'markdown' ? 'active' : ''}`}><FaMarkdown
                      className="tab-icon"/> Markdown
                  </button>
                </div>

                <motion.div className="tab-content" key={activeTab} initial={{opacity: 0}} animate={{opacity: 1}}
                            transition={{duration: 0.3}}>
                  {activeTab === 'preview' ? (
                      <div className="preview-container markdown-preview">
                        <ReactMarkdown rehypePlugins={[rehypeRaw]} components={components}
                                       className="prose prose-slate max-w-none">{blogData.markdown}</ReactMarkdown>
                      </div>
                  ) : (
                      <div className="markdown-container">
                        <button onClick={copyToClipboard}
                                className={`copy-button ${copySuccess ? 'success' : ''}`}>{copySuccess ? <> <FaCheck
                            className="button-icon"/> Copied!</> : <> <FaCopy className="button-icon"/> Copy
                          markdown</>}</button>
                        <pre className="markdown-source">{blogData.markdown}</pre>
                      </div>
                  )}
                </motion.div>
              </motion.div>
          )}
        </AnimatePresence>
      </div>

      <footer className="app-footer"><p>Recipe Blog Generator © {new Date().getFullYear()}</p></footer>
    </div>
  );
}

export default App;