import React from 'react';
import clsx from 'clsx';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import useBaseUrl from '@docusaurus/useBaseUrl';
import styles from './styles.module.css';

const features = [
  {
    title: 'Use Jupyter Notebooks',
    imageUrl: 'img/Jupyter_logo.svg',
    description: (
      <>
        Use everyone's favourite literate programing tool... Jupyter Notebooks!
        No more copying and pasting code from the terminal to markdown. Keep
        your code and writing all in one place.
      </>
    ),
  },
  {
    title: 'Use Markdown',
    imageUrl: 'img/Markdown-mark.svg',
    description: (
      <>
        The easiest to read and write markup language. No more googling how to
        use again.
      </>
    ),
  },
  {
    title: 'BYOSSG',
    imageUrl: 'img/world-wide-web.svg',
    description: (
      <>
        Bring your own static site generator (BYOSSG). jupydocs simply exports
        your docstrings into markdown, so you can host your site using any
        static site generator.
      </>
    ),
  },
];

function Feature({imageUrl, title, description}) {
  const imgUrl = useBaseUrl(imageUrl);
  return (
    <div className={clsx('col col--4', styles.feature)}>
      {imgUrl && (
        <div className="text--center">
          <img className={styles.featureImage} src={imgUrl} alt={title} />
        </div>
      )}
      <h3>{title}</h3>
      <p>{description}</p>
    </div>
  );
}

function Home() {
  const context = useDocusaurusContext();
  const {siteConfig = {}} = context;
  return (
    <Layout
      title={''}
      description="jupydocs - easy python package documentation using markdown and jupyter">
      <header className={clsx('hero hero--primary', styles.heroBanner)}>
        <div className="container">
          {/* <h1 className="hero__title">{siteConfig.title}</h1> */}
          <div>
            <img src={"img/jupydocs_logo_white_text.png"} alt={"logo"} />
          </div>
          <p className="hero__subtitle">{siteConfig.tagline}</p>
          <div className={styles.buttons}>
            <Link
              className={clsx(
                'button button--outline button--secondary button--lg',
                styles.getStarted,
              )}
              to={useBaseUrl('docs/')}>
              Get Started
            </Link>
          </div>
        </div>
      </header>
      <main>
        {features && features.length > 0 && (
          <section className={styles.features}>
            <div className="container">
              <div className="row">
                {features.map((props, idx) => (
                  <Feature key={idx} {...props} />
                ))}
              </div>
            </div>
          </section>
        )}
      </main>
    </Layout>
  );
}

export default Home;
