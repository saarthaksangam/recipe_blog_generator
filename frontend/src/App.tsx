import { useState, useEffect } from 'react';
import ReactMarkdown from 'react-markdown';
import rehypeRaw from 'rehype-raw';
import { motion, AnimatePresence } from 'framer-motion';
import './markdown-styles.css';
import './animations.css';

// Import icons
import { FaYoutube, FaCopy, FaCheck, FaCog, FaMarkdown } from 'react-icons/fa';
import { HiSparkles, HiOutlineDocumentText } from 'react-icons/hi';

// Define TypeScript interfaces for our data
interface BlogData {
  title: string;
  markdown: string;
  upload_date: string;
  thumbnail_url: string;
  youtube_url: string;
}

// Loading messages to cycle through
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
  const getYoutubeEmbedUrl = (url: string): string => {
    const regExp = /^.*((youtu.be\/)|(v\/)|(\/u\/\w\/)|(embed\/)|(watch\?))\??v?=?([^#&?]*).*/;
    const match = url.match(regExp);
    const videoId = (match && match[7].length === 11) ? match[7] : '';
    return `https://www.youtube.com/embed/${videoId}?enablejsapi=1`;
  };

  // Cycle through loading messages and progress
  useEffect(() => {
    if (!isLoading) return;

    let messageIndex = 0;
    let progress = 0;
    let startTime = Date.now();
    let errorMessageShown = false;

    setLoadingMessage(loadingMessages[0]);

    const messageInterval = setInterval(() => {
      const elapsed = Date.now() - startTime;
      if (elapsed > 45000 && !errorMessageShown) {
        setLoadingMessage("Something seems to be wrong. The server might be busy...");
        errorMessageShown = true;
        return;
      }
      if (errorMessageShown) return;
      messageIndex = Math.min(messageIndex + 1, loadingMessages.length - 1);
      setLoadingMessage(loadingMessages[messageIndex]);
      if (messageIndex === loadingMessages.length - 1) clearInterval(messageInterval);
    }, 1600);

    const progressInterval = setInterval(() => {
      const increment = 95 - progress > 50 ? 5 : (95 - progress > 20 ? 3 : 1);
      progress = Math.min(progress + increment, 95);
      setLoadingProgress(progress);
    }, 800);

    return () => {
      clearInterval(messageInterval);
      clearInterval(progressInterval);
      setLoadingProgress(0);
    };
  }, [isLoading]);

  // Handle form submission
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!youtubeUrl.includes('youtube.com/watch') && !youtubeUrl.includes('youtu.be')) {
      setError('Please enter a valid YouTube URL');
      return;
    }
    try {
      setIsLoading(true);
      setError(null);
      const response = await fetch(`http://localhost:8000/api/v1/generate-blog?youtube_url=${encodeURIComponent(youtubeUrl)}`);
      if (!response.ok) {
        const err = await response.json();
        throw new Error(err.detail || 'Failed to generate blog post');
      }
      const data = await response.json();
      setBlogData(data);
      setLoadingProgress(100);
      setTimeout(() => setIsLoading(false), 500);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An unknown error occurred');
      setIsLoading(false);
    }
  };

  // Copy markdown to clipboard
  const copyToClipboard = () => {
    if (!blogData) return;
    navigator.clipboard.writeText(blogData.markdown)
      .then(() => {
        setCopySuccess(true);
        setTimeout(() => setCopySuccess(false), 2000);
      })
      .catch(console.error);
  };

  // Custom components for ReactMarkdown
  const components = {
    img: ({node, ...props}) => (
      <motion.img
        initial={{ opacity: 0, scale: 0.95 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ duration: 0.5 }}
        {...props}
        className="markdown-image"
      />
    ),

    iframe: ({node, ...props}) => {
      if (props.src && props.src.includes('youtube.com')) {
        const videoUrl = props.src.includes('/embed/')
          ? props.src
          : getYoutubeEmbedUrl(props.src);
        return (
          <div className="youtube-iframe-container">
            <iframe
              {...props}
              src={videoUrl}
              frameBorder="0"
              allowFullScreen
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
              className="youtube-iframe"
            />
          </div>
        );
      }
      return <iframe {...props} />;
    },

    blockquote: ({node, ...props}) => {
      // Extract and clean up content
      let content = '';
      if (node.children) {
        node.children.forEach((child: any) => {
          if (child.children) {
            child.children.forEach((textNode: any) => {
              if (textNode.value) content += textNode.value;
            });
          }
        });
      }
      content = content.replace(/^"/, '').replace(/"$/, '');

      const isMetadataBlock =
        content.includes('Posted on Youtube') ||
        content.includes('By ') ||
        content.includes('Recipes that impress');

      if (isMetadataBlock) {
        return (
          <motion.blockquote
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5 }}
            className="metadata-blockquote"
          >
            {content.includes('Posted on Youtube') && (
              <p>
                <FaYoutube className="inline-icon" />
                Posted on {content.match(/on (\d{4}-\d{2}-\d{2})/)?.[1] || ''}
              </p>
            )}
            {content.includes('By ') && (
              <p>By {content.match(/By ([^R]+)/)?.[1].trim()}</p>
            )}
            {content.includes('Recipes that') && (
              <p><span className="tagline">Recipes that impress with ease</span></p>
            )}
          </motion.blockquote>
        );
      }
      return <blockquote {...props} />;
    },
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

        <motion.div className="content-area" initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ delay: 0.2, duration: 0.5 }}>
          <motion.div className="input-container" whileHover={{ boxShadow: "0 8px 30px rgba(0,0,0,0.12)" }} transition={{ duration: 0.3 }}>
            <form onSubmit={handleSubmit}>
              <div className="input-wrapper">
                <div className="input-icon-wrapper">
                  <FaYoutube className="input-icon" />
                  <input type="url" value={youtubeUrl} onChange={e => setYoutubeUrl(e.target.value)} placeholder="Paste YouTube URL here..." className="url-input" required />
                </div>
                <button type="submit" className="submit-button" disabled={isLoading}>
                  {isLoading ? 'Processing...' : 'Generate Blog'}
                </button>
              </div>
              {error && (
                <motion.div className="error-message" initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }}>
                  {error}
                </motion.div>
              )}
            </form>
          </motion.div>

          <AnimatePresence>
            {isLoading && (
              <motion.div className="loading-container" initial={{ opacity: 0, scale: 0.95 }} animate={{ opacity: 1, scale: 1 }} exit={{ opacity: 0, scale: 0.9 }} transition={{ duration: 0.3 }}>
                <div className="loader-content">
                  <div className="spinner-container"><div className="spinner"><FaCog className="spinner-icon" /></div></div>
                  <div className="loading-text-container">
                    <motion.h3 className="loading-message" key={loadingMessage} initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} exit={{ opacity: 0, y: -10 }} transition={{ duration: 0.5 }}>{loadingMessage}</motion.h3>
                    <div className="progress-bar-container"><div className="progress-bar" style={{ width: `${loadingProgress}%` }}></div></div>
                  </div>
                </div>
              </motion.div>
            )}

            {blogData && !isLoading && (
              <motion.div className="result-container" initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.5 }}>
                <div className="tabs">
                  <button onClick={() => setActiveTab('preview')} className={`tab ${activeTab === 'preview' ? 'active' : ''}`}><HiOutlineDocumentText className="tab-icon" /> Preview</button>
                  <button onClick={() => setActiveTab('markdown')} className={`tab ${activeTab === 'markdown' ? 'active' : ''}`}><FaMarkdown className="tab-icon" /> Markdown</button>
                </div>

                <motion.div className="tab-content" key={activeTab} initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ duration: 0.3 }}>
                  {activeTab === 'preview' ? (
                    <div className="preview-container markdown-preview">
                      <ReactMarkdown rehypePlugins={[rehypeRaw]} components={components} className="prose prose-slate max-w-none">{blogData.markdown}</ReactMarkdown>
                    </div>
                  ) : (
                    <div className="markdown-container">
                      <button onClick={copyToClipboard} className={`copy-button ${copySuccess ? 'success' : ''}`}>{copySuccess ? <><FaCheck className="button-icon" /> Copied!</> : <><FaCopy className="button-icon" /> Copy markdown</>}</button>
                      <pre className="markdown-source">{blogData.markdown}</pre>
                    </div>
                  )}
                </motion.div>
              </motion.div>
            )}
          </AnimatePresence>
        </motion.div>
      </div>

      <footer className="app-footer">
        <p>Recipe Blog Generator &copy; {new Date().getFullYear()}</p>
      </footer>
    </div>
  );
}

export default App;
