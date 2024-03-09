import Image from "next/image";
import styles from "./page.module.css";
import Contents from "./contents/page";


export default function Home() {

  return (
    <>
      <main className={styles.main}>
        <div>File Storage</div>
        <ul>
          <Contents />
        </ul>
      </main>
    </>
  );
}
